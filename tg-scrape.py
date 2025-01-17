# tg-scrape.py

import config

from telethon.sync import TelegramClient
import asyncio
import sqlite3
import re
import requests

# Create the tokens table if it doesn't exist. Will add more columns later on
def create_new_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tokens (
        id INTEGER PRIMARY KEY,
        chat_name TEXT,
        chat_id INTEGER,
        message_text TEXT,
        token_symbol TEXT
        )
        ''')

# Drop the tokens table
def drop_table(cursor):
    cursor.execute('''
        DROP TABLE IF EXISTS tokens
        ''')

# Pull token address from Helius API
def get_token_address(token_symbol):
    try: 
        # Set API endpoint and parameters
        endpoint = f"https://mainnet.helius-rpc.com/?api-key={hel_api_key}"

        # Set request package
        response = requests.post(
            endpoint,
            headers = {"Content-Type": "application/json"},
            json = {
                "jsonrpc": "2.0",
                "id": "get_token_address",
                "method": "getAsset",
                "params": {"symbol": token_symbol}
            }
        )

        # Check if response was sucessful
        if response.status_code == 200:
            # Parse response
            data = response.json()

            # Extract token balance from response
            token_address = data["result"]["id"]

            return token_address
    
    except requests.exceptions.RequestException as e: 
        # Handle request exception 
        print(f"Error: {e}")
        return None

# Pull token supply from Helius API
def get_token_supply(token_address):
    try: 
        # Set API endpoint 
        endpoint = f"https://mainnet.helius-rpc.com/?api-key={hel_api_key}"
        
        # Set request package
        response = requests.post(
            endpoint,
            headers = {"Content-Type": "application/json"},
            json = {
                "jsonrpc": "2.0",
                "id": "get_token_supply",
                "method": "getAsset",
                "params": {"id": token_address}
            }
        )

        # Check if response was sucessful
        if response.status_code == 200:
            # Parse response
            data = response.json()

            # Extract token balance from response
            token_supply = data["result"]["supply"]["print_max_supply"]

            return token_supply
    
        else:
            # Handle API error
            print(f"Error: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        # Handle request exception 
        print(f"Error: {e}")
        return None

# Pull token price
def get_token_price(token_address):
    try: 
        # Set API endpoint
        endpoint = f"https://mainnet.helius-rpc.com/?api-key={hel_api_key}"

        # Set request package
        response = requests.post(
            endpoint,
            headers = {"Content-Type": "application/json"},
            json = {
                "jsonrpc": "2.0",
                "id": "get_token_price",
                "method": "getAsset",
                "params": {"id": token_address}
            }
        )

        # Check if response was sucessful
        if response.status_code == 200:
            # Parse response
            data = response.json()

            # Extract token balance from response
            token_price = data["result"]["price"] # Confirm whether this is the right path
        
            return token_price
        
        else:
            # Handle API error
            print(f"Error: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        # Handle request exception 
        print(f"Error: {e}")
        return None

# Calculate token FDV
def calculate_token_fdv(token_price, token_supply):
    try: 
        token_fdv = token_price * token_supply
        return token_fdv
    
    except requests.exceptions.RequestException as e:
        # Handle request exception 
        print(f"Error: {e}")
        return None

    except ZeroDivisionError:
        print("Error: Division by zero")
        return None

    except Exception as e:
        print(f"Error: {e}")
        return None

# Inserting data into table
def insert_data(cursor, chat_name, chat_id, message_text, token_symbol):
    try:
        cursor.execute('''
                        INSERT INTO tokens (chat_name, chat_id, message_text, token_symbol)
                        VALUES (?, ?, ?, ?)
                        ''', (chat_name, chat_id, message_text,token_symbol))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")

# Printing results of table
def print_data(cursor):
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Replace your API ID and API Hash
tg_api_id = config.tg_api_id
tg_api_hash = config.tg_api_hash
hel_api_key = config.hel_api_key

# Connect to the SQLite database
conn = sqlite3.connect('tg-scrape.db')
cursor = conn.cursor()

# Create table tokens
create_new_table(cursor)

# Create a TelegramClient
client = TelegramClient('tg-scrape', tg_api_id, tg_api_hash)

# Authenticate the client
async def main():
    await client.start()

    # Get all chat ids
    chats = await client.get_dialogs()
    chat_info = {}

    # Store them in a dictionary (both title and id)
    for chat in chats:
        chat_info[chat.id] = {
            'title': chat.title,
        }

    # Fetch messages from each chat
    for chat_id, chat_data in chat_info.items():
        messages = await client.get_messages(chat_id, limit=100)
        for message in messages:

            # Parse the messages and extract token mentions starting with "$"
            extracted_tokens = re.findall(r'\$\w+', message.text)

            # Store token mentions into database
            for token in extracted_tokens:
                
                # Get token address
                address = get_token_address(token[1:])

                # Calculate token FDV
                fdv = calculate_token_fdv(address, get_token_price(address), get_token_supply(address))
                print(fdv)

                insert_data(cursor, chat_data['title'], chat_id, message.text, token[1:])

            # Print the results
            print_data(cursor)

            await asyncio.sleep(1)

    # Close the database connection
    conn.close()

with client:
    client.loop.run_until_complete(main())
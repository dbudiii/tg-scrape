# tg-scrape.py

import config

from telethon.sync import TelegramClient
import asyncio
import sqlite3
import re

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

# [TODO]Pull token address from Helius API
def get_token_address(token_symbol):
    try: 
        pass 
    except: 
        pass

# [TODO]Pull token supply from Helius API
def get_token_supply(token_symbol):
    try: 
        return token_supply
    except: 
        pass

# [TODO]Pull token price
def get_token_price(token_symbol):
    try: 
        return token_price
    except: 
        pass

# [TODO]Calculate token FDV
def calculate_token_fdv(token_symbol):
    try: 
        token_fdv = token_supply * token_price
        return token_fdv
    except: 
        pass

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
                insert_data(cursor, chat_data['title'], chat_id, message.text, token[1:])

            # Print the results
            print_data(cursor)

            await asyncio.sleep(1)

    # Close the database connection
    conn.close()

with client:
    client.loop.run_until_complete(main())
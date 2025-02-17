# coin functions
import re
import requests
from telethon.sync import TelegramClient
import asyncio


### Main Functions ###

# Fetch chat dialogs, store them in messages list, and return messages list. We use get_messages to have more control over retrieval and filtering of messages
async def fetch_messages(client):
    try:
        chats = await client.get_dialogs() 
        messages = []
        for chat in chats:
            chat_messages = await client.get_messages(chat.id, limit=100)
            messages.extend(chat_messages)
        return messages

    except Exception as e:
        print(f"Error: {e}")

def extract_addresses(message):
    solana_regex = r'^[1-9A-HJ-NP-Za-km-z]{32}$'
    return re.findall(solana_regex, message)

### coin API Functions ###
# Pull coin address from Helius API
def get_coin_symbol(coin_address):
    try: 
        # Set API endpoint and parameters
        endpoint = f"https://mainnet.helius-rpc.com/?api-key={hel_api_key}"

        # Set request package
        response = requests.post(
            endpoint,
            headers = {"Content-Type": "application/json"},
            json = {
                "jsonrpc": "2.0",
                "id": "get_coin_symbol",
                "method": "getAsset",
                "params": {"id": f"{coin_address}"}
            }
        )

        # Check if response was sucessful
        if response.status_code == 200:
            # Parse response
            data = response.json()

            # Extract coin symbol from response
            coin_symbol = data["result"]["content"]["metadata"]["symbol"]

            return coin_symbol
    
    except requests.exceptions.RequestException as e: 
        # Handle request exception 
        print(f"Error: {e}")
        return None

# Pull coin supply from Helius API [DONE]
def get_coin_supply(coin_address):
    try: 
        # Set API endpoint 
        endpoint = f"https://mainnet.helius-rpc.com/?api-key={hel_api_key}"
        
        # Set request package
        response = requests.post(
            endpoint,
            headers = {"Content-Type": "application/json"},
            json = {
                "jsonrpc": "2.0",
                "id": "get_coin_supply",
                "method": "getAsset",
                "params": {"id": f"{coin_address}"}
            }
        )

        # Check if response was sucessful
        if response.status_code == 200:
            # Parse response
            data = response.json()

            # Extract coin balance from response
            coin_supply = data["result"]["supply"]["print_max_supply"]

            return coin_supply
    
        else:
            # Handle API error
            print(f"Error: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        # Handle request exception 
        print(f"Error: {e}")
        return None

# Pull coin price
def get_coin_price(coin_address):
    try: 
        # Set API endpoint
        endpoint = f"https://mainnet.helius-rpc.com/?api-key={hel_api_key}"

        # Set request package
        response = requests.post(
            endpoint,
            headers = {"Content-Type": "application/json"},
            json = {
                "jsonrpc": "2.0",
                "id": "get_coin_price",
                "method": "getAsset",
                "params": {"id": f"{coin_address}"}
            }
        )

        # Check if response was sucessful
        if response.status_code == 200:
            # Parse response
            data = response.json()

            # Extract coin balance from response
            coin_price = data["result"]["price"] # Confirm whether this is the right path
        
            return coin_price
        
        else:
            # Handle API error
            print(f"Error: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        # Handle request exception 
        print(f"Error: {e}")
        return None

# Calculate coin FDV
def calculate_coin_fdv(coin_price, coin_supply):
    try: 
        coin_fdv = coin_price * coin_supply
        return coin_fdv
    
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

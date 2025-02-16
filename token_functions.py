# Token functions
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


### Token API Functions ###
# Pull token address from Helius API [UPDATE SYMBOL TO ADDRESS - UNIVERSAL]
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

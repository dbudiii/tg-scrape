# tg-scrape.py

import config
import DB_Connection
import DB_Schema
import DB_Actions 
from token_functions import *
from telethon.sync import TelegramClient
import asyncio
import sqlite3
import re

# Replace your API ID and API Hash
tg_api_id = config.tg_api_id
tg_api_hash = config.tg_api_hash
hel_api_key = config.hel_api_key

# Create a TelegramClient
client = TelegramClient('tg-scrape', tg_api_id, tg_api_hash)

# Authenticate the client
async def main():
    await client.start()

    # Fetch messages from each chat and store them in message variable to set up for parsing. 
    messages = await fetch_messages(client)

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
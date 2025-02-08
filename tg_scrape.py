# tg-scrape.py

import config
import DB_Connection
import DB_Schema
import DB_Actions
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
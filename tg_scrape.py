# tg-scrape.py

import config
from .DB.DB_Connection import *
from DB.DB_Schema import *
from DB.DB_Actions import * 
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
client = TelegramClient('tg_scrape', tg_api_id, tg_api_hash)

# Authenticate the client
async def main():
    await client.start()

    # Fetch messages from each chat and store them in message variable to set up for parsing. 
    messages = await fetch_messages(client)

    for message in messages:
        # Parse the messages and extract token addresses and put into list
        coin_addresses = extract_addresses(message)

    test_list = []
    for address in coin_addresses:
        get_coin_symbol(address)

with client:
    client.loop.run_until_complete(main())
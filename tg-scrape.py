# tg-scrape.py

import config

from telethon.sync import TelegramClient
import asyncio
import sqlite3

# Replace your API ID and API Hash
api_id = config.api_id
api_hash = config.api_hash

# Connect to the SQLite database
conn = sqlite3.connect('tg-scrape.db')
cursor = conn.cursor()

# Create the tokens table if it doesn't exist. Will add more columns later on
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tokens (
        id INTEGER PRIMARY KEY,
        chat_id INTEGER,
        message_text TEXT,
        token_name TEXT,
        token_symbol TEXT
    )
''')

# Create a TelegramClient
client = TelegramClient('tg-scrape', api_id, api_hash)

# Authenticate the client
async def main():
    await client.start()

    # Get all chat ids
    chats = await client.get_dialogs()
    chat_ids = {}

    # Store them in a dictionary (both title and id)
    for chat in chats:
        chat_ids[chat.title] = chat.id
        
    # Fetch messages from each chat
    for chat_tittle, chat_id in chat_ids.items():
        messages = await client.get_messages(chat_id, limit=100)
        for message in messages:

            # Insert logic to parse and store messages in database here
            print(message.text)

            await asyncio.sleep(1)

with client:
    client.loop.run_until_complete(main())
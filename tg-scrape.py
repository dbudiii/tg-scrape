# tg-scrape.py

import config

from telethon.sync import TelegramClient
import asyncio
import sqlite3
import re

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
        chat_name TEXT,
        chat_id INTEGER,
        message_text TEXT,
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
    # May need to update this and the above so that we are storing both the id and title as values in the dictionary
    for chat in chats:
        chat_ids[chat.title] = chat.id
        
    # Fetch messages from each chat
    # Need to update this if we are updating the dictionary pulls above
    for chat_title, chat_id in chat_ids.items():
        messages = await client.get_messages(chat_id, limit=100)
        for message in messages:

            # Parse the messages and extract token mentions starting with "$"
            token_mentions = re.findall(r'\$\w+', message.text)

            # Store token mentions into database
            for token in token_mentions:
                cursor.execute('''
                               INSERT INTO tokens (chat_name, chat_id, message_text, token_symbol)
                               VALUES (?, ?, ?, ?)
                               ''', (chat_title, chat_id, message.text,token[1:]))
                conn.commit()

            rows = cursor.fetchall()
            for row in rows:
                print(row)

            await asyncio.sleep(1)

with client:
    client.loop.run_until_complete(main())
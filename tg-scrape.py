# tg-scrape.py

import config

from telethon.sync import TelegramClient
import asyncio

api_id = config.api_id
api_hash = config.api_hash

client = TelegramClient('tg-scrape', api_id, api_hash)

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
        messages = await client.get_messages(chat_id)
        for message in messages:

            # Insert logic to parse and store messages in database here
            print(message.text)

with client:
    client.loop.run_until_complete(main())
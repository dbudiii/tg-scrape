# tg-scrape.py

import config
from DB.DB_Connection import *
from DB.DB_Schema import *
from DB.DB_Actions import * 
from token_functions import *
from telethon.sync import TelegramClient


# Global Variables 
tg_api_id = config.tg_api_id
tg_api_hash = config.tg_api_hash

# Create a TelegramClient
client = TelegramClient('tg_scrape', tg_api_id, tg_api_hash)

# Authenticate the client
async def main():
    await client.start()

    # Fetch messages from each chat and store them in message variable to set up for parsing. 
    messages = await fetch_messages(client)

    coin_data = {}
    for message in messages:
        # Parse the messages, extract token address, add address and timestamp to coin_data dict
        addresses = extract_addresses(message.text)
        if addresses:
            for address in addresses:
                timestamp = message.date
                coin_data[address] = timestamp

    # Create connection to database
    cursor = get_connection()

    # Create table if not created
    table_name = 'tokens'
    create_table(cursor, table_name)

    # Insert data into database
    for address, timestamp in coin_data.items():
        insert_data(cursor, address, timestamp)

    get_token_counts(cursor, table_name)

    # Close connection
    conn.commit()
    conn.close()

if __name__ == '__main__':

    # Execute main loop
    with client:
        client.loop.run_until_complete(main())
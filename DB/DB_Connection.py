# DB Connection
import sqlite3

DB_PATH = 'tg_scrape.db'
conn = sqlite3.connect(DB_PATH)

# Connect to the SQLite database
def get_connection():
    cursor = conn.cursor()
    return cursor 
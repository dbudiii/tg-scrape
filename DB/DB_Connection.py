# DB Connection
import sqlite3

DB_PATH = 'tg_scrape.db'

# Connect to the SQLite database
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    return cursor 
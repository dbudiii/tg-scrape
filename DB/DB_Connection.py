# DB Connection
import sqlite3


DB_PATH = 'tg_scrape.db'
conn = sqlite3.connect(DB_PATH)

# Connect to the SQLite database
def get_connection():
    cursor = conn.cursor()
    return cursor 

# To alter the table schema
# cursor = get_connection()
# cursor.execute('''CREATE TABLE tokens_new (id INTEGER PRIMARY KEY, token_address TEXT, timestamp TEXT)''')
# cursor.execute('''DROP TABLE tokens''')
# cursor.execute('''ALTER TABLE tokens_new RENAME TO tokens''')
# conn.commit()
# conn.close()
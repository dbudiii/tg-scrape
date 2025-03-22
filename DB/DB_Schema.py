# DB Schema
from .DB_Connection import *

# Create the tokens schema if it doesn't exist
def create_table(cursor, table_name):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS {} (
        id INTEGER PRIMARY KEY,
        token_address TEXT,
        timestamp TEXT,
        UNIQUE (token_address, timestamp)
        )
        '''.format(table_name))
    

# To alter the table schema
# cursor = get_connection()
# cursor.execute('''CREATE TABLE tokens_new (id INTEGER PRIMARY KEY, token_address TEXT, timestamp TEXT, UNIQUE (token_address, timestamp))''')
# cursor.execute('''DROP TABLE tokens''')
# cursor.execute('''ALTER TABLE tokens_new RENAME TO tokens''')
# conn.commit()
# conn.close()
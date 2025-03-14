# DB Schema

# Create the tokens schema if it doesn't exist
def create_table(cursor, table_name):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS {} (
        id INTEGER PRIMARY KEY,
        chat_name TEXT,
        chat_id INTEGER,
        message_text TEXT,
        token_address TEXT
        )
        '''.format(table_name))
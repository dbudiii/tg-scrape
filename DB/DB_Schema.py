# DB Schema

# Create the tokens schema if it doesn't exist [EDIT SCHEMA]
def create_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tokens (
        id INTEGER PRIMARY KEY,
        chat_name TEXT,
        chat_id INTEGER,
        message_text TEXT,
        token_symbol TEXT
        )
        ''')
# DB Schema

# Create the tokens schema if it doesn't exist
def create_table(cursor, table_name):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS {} (
        id INTEGER PRIMARY KEY,
        token_address TEXT,
        timestamp TEXT
        )
        '''.format(table_name))
    
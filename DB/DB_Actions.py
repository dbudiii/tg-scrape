# DB Actions

import sqlite3
from DB_Connection import get_connection

# Takes an SQL query input and makes it easy to execute
def execute_query(query):
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print(f"Error executing query: {e}")
        return None

# Drop the table, executed through execute_query
def drop_table(table_name):
    query = "DROP TABLE IF EXISTS {table_name};".format(table_name=table_name)
    return execute_query(query)

# Read the table, executed through execute_query
def read_table(table_name):
    query = "SELECT * FROM {table_name};".format(table_name=table_name)
    results = execute_query(query)
    for row in results:
        print(row)

# Inserting data into table through execute_query [UPDATE]
def insert_data(cursor, chat_name, chat_id, message_text, token_symbol):
    try:
        cursor.execute('''
                    INSERT INTO tokens (chat_name, chat_id, message_text, token_symbol)
                    VALUES (?, ?, ?, ?)
                    ''', (chat_name, chat_id, message_text,token_symbol))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")
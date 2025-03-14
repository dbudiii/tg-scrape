# DB Actions

import sqlite3
from DB.DB_Connection import *

# Takes an SQL query input and makes it easy to execute
def execute_query(cursor, query):
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
def read_table(cursor, table_name):
    query = "SELECT * FROM {table_name};".format(table_name=table_name)
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except sqlite3.Error as e:
        print(f"Error executing query: {e}")
        return None

# Inserting data into table through execute_query [UPDATE]
def insert_data(cursor, chat_name, chat_id, message_text, token_address):
    try:
        cursor.execute('''
                    INSERT INTO tokens (chat_name, chat_id, message_text, token_address)
                    VALUES (?, ?, ?, ?)
                    ''', (chat_name, chat_id, message_text,token_address))
        cursor.commit()
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")
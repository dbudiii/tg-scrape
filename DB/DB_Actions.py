# DB Actions

import sqlite3
from DB.DB_Connection import *

# Updated Insert data

# Drop the table, executed through execute_query
def drop_table(cursor, table_name):
    query = "DROP TABLE IF EXISTS {table_name};".format(table_name=table_name)
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"Error executing query: {e}")
        return None

# Read the table, executed through execute_query [TO DELETE]
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
def insert_data(cursor, data):
    try:
        cursor.executemany('''
                    INSERT INTO tokens (id, token_address, timestamp)
                    VALUES (?, ?, ?, ?)
                    ''', data)
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")
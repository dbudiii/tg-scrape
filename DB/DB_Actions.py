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

# Inserting data into table; checks that the address and timestamp are unique to create a new entry so
# that the data is not duplicated for every time we run it
def insert_data(cursor, address, timestamp):
    try:
        cursor.execute('''
                    INSERT OR IGNORE INTO tokens (id, token_address, timestamp)
                    VALUES (NULL, ?, ?)
                    ''', (address, timestamp))
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")

def get_token_counts(cursor, table_name):
    cursor.execute('''
        SELECT token_address, COUNT(*) as mention_count
        FROM tokens
        GROUP BY token_address
        ORDER BY mention_count DESC
        LIMIT 5
    ''')

    results = cursor.fetchall()
    for address, count in results:
        print(f"Address: {address}, Mention Count: {count}")
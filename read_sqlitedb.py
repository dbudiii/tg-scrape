import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('tg-scrape.db')
cursor = conn.cursor()

# Run a SELECT query
cursor.execute('SELECT * FROM tokens')

# Fetch the results
results = cursor.fetchall()

# Print the results
for result in results:
    print(result)

# # Get column names
# cursor.execute("PRAGMA table_info(tokens)")
# columns = cursor.fetchall()

# # Print column details
# for column in columns:
#     print(f"Column ID: {column[0]}, Name: {column[1]}, Type: {column[2]}")

# Close the connection
conn.close()
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

# Close the connection
conn.close()
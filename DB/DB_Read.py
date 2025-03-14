# Check DB

from DB.DB_Connection import *

# Get connection
cursor = get_connection()

# Checking databse file
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print('Tables in the database: ', tables)

# Checking table structure
cursor.execute("PRAGMA table_info(tokens)")
columns = cursor.fetchall()
print("Column info: ", columns)

# View contents of table
cursor.execute("SELECT * FROM tokens")
data = cursor.fetchall()
print("Table contents: ", data)

# Close the database connection
conn.close()
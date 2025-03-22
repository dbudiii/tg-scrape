# Check DB

from DB_Connection import *

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

# View contents of table in chronological order
cursor.execute('''   
    SELECT * FROM tokens
    ORDER BY timestamp ASC
    ''')

data = cursor.fetchall()
print("Table contents: \n") 
for row in data:
    print(row)
    
# Close the database connection
conn.close()
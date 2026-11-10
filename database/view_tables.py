
from database.db_connection import get_connection

# Connect to database
connection = get_connection()

# Create cursor
cursor = connection.cursor()

# Get all table names
cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type = 'table'
""")

tables = cursor.fetchall()

# Display table names
print("Tables in SmartSpend Database:")

for table in tables:
    print(table[0])

connection.close()

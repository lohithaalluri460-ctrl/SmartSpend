
from database.db_connection import get_connection

print("===== SMARTSPEND DATABASE TEST =====")

connection = get_connection()
cursor = connection.cursor()

# 1. Check database tables
print("\n1. Checking database tables")

cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type = 'table'
AND name NOT LIKE 'sqlite_%'
""")

tables = cursor.fetchall()

for table in tables:
    print("Table:", table[0])

# 2. Check registered users
print("\n2. Checking users")

cursor.execute("""
SELECT user_id, name, email
FROM users
""")

users = cursor.fetchall()

for user in users:
    print(user)

# 3. Check expenses
print("\n3. Checking expenses")

cursor.execute("""
SELECT expense_id, user_id, amount, category, expense_date
FROM expenses
""")

expenses = cursor.fetchall()

for expense in expenses:
    print(expense)

# 4. Check budgets
print("\n4. Checking budgets")

cursor.execute("""
SELECT budget_id, user_id, month, year, amount
FROM budgets
""")

budgets = cursor.fetchall()

for budget in budgets:
    print(budget)

connection.close()

print("\n===== DATABASE TEST COMPLETED =====")

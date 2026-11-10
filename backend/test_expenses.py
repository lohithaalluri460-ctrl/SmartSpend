
from backend.expense_service import add_expense

print("SMARTSPEND - ADD EXPENSE")

user_id = int(input("Enter user ID: "))
amount = float(input("Enter amount: "))
category = input("Enter category: ")
description = input("Enter description: ")
expense_date = input("Enter date (YYYY-MM-DD): ")

success, message = add_expense(
    user_id,
    amount,
    category,
    description,
    expense_date
)

print(message)

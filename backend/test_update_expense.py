
from backend.expense_service import update_expense

print("SMARTSPEND - UPDATE EXPENSE")

user_id = int(input("Enter your user ID: "))
expense_id = int(input("Enter expense ID to update: "))

amount = float(input("Enter new amount: "))
category = input("Enter new category: ")
description = input("Enter new description: ")
expense_date = input("Enter new date (YYYY-MM-DD): ")

success, message = update_expense(
    expense_id,
    user_id,
    amount,
    category,
    description,
    expense_date
)

print(message)

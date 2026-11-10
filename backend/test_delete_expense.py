
from backend.expense_service import delete_expense

print("SMARTSPEND - DELETE EXPENSE")

user_id = int(input("Enter your user ID: "))
expense_id = int(input("Enter expense ID to delete: "))

confirm = input("Are you sure? (yes/no): ")

if confirm.lower() == "yes":

    success, message = delete_expense(
        expense_id,
        user_id
    )

    print(message)

else:
    print("Deletion cancelled.")

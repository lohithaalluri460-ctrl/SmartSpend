
from backend.expense_service import get_user_expenses

print("SMARTSPEND - VIEW EXPENSES")

user_id = int(input("Enter your user ID: "))

expenses = get_user_expenses(user_id)

if not expenses:

    print("No expenses found.")

else:

    print("\nYour Expenses:")

    print("-" * 70)

    for expense in expenses:

        print("Expense ID:", expense[0])
        print("Amount:", expense[1])
        print("Category:", expense[2])
        print("Description:", expense[3])
        print("Date:", expense[4])

        print("-" * 70)

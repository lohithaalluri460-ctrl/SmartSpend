
from backend.expense_service import get_expense_summary_by_category

print("SMARTSPEND - CATEGORY-WISE EXPENSE SUMMARY")

user_id = int(input("Enter your user ID: "))
month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

summary = get_expense_summary_by_category(
    user_id, month, year
)

if not summary:
    print("No expenses found for this month.")
else:
    print("\nCategory-wise Expenses:")

    for category, total in summary:
        print(category, ":", total)


from backend.budget_service import get_monthly_budget

print("SMARTSPEND - VIEW MONTHLY BUDGET")

user_id = int(input("Enter your user ID: "))
month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

budget = get_monthly_budget(user_id, month, year)

if budget is None:
    print("No budget found for this month.")
else:
    print("Your monthly budget is:", budget)

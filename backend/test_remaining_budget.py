
from backend.budget_service import get_remaining_budget

print("SMARTSPEND - REMAINING BUDGET")

user_id = int(input("Enter your user ID: "))
month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

remaining, result = get_remaining_budget(
    user_id, month, year
)

if remaining is None:
    print(result)
else:
    print("Total expenses:", result)
    print("Remaining budget:", remaining)

    if remaining < 0:
        print("Warning: You have exceeded your budget!")

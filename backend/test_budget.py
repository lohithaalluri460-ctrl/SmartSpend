
from backend.budget_service import set_budget

print("SMARTSPEND - SET MONTHLY BUDGET")

user_id = int(input("Enter your user ID: "))
month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))
amount = float(input("Enter monthly budget: "))

success, message = set_budget(
    user_id,
    month,
    year,
    amount
)

print(message)

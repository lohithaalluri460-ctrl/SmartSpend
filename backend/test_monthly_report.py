
from backend.budget_service import generate_monthly_report

print("SMARTSPEND - MONTHLY EXPENSE REPORT")

user_id = int(input("Enter your user ID: "))
month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

report = generate_monthly_report(user_id, month, year)

if report is None:
    print("Please set a monthly budget first.")

else:
    print("\n========== MONTHLY REPORT ==========")

    print("Monthly Budget:", report["budget"])
    print("Total Expenses:", report["total_expenses"])
    print("Remaining Budget:", report["remaining"])

    if report["remaining"] < 0:
        print("Warning: Budget exceeded!")
    else:
        print("Budget Status: Within budget")

    print("\nCategory-wise Expenses:")

    if report["category_summary"]:
        for category, amount in report["category_summary"]:
            print(category, ":", amount)
    else:
        print("No expenses recorded.")

    print("====================================")

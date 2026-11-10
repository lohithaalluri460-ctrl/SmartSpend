
from backend.auth import register_user, login_user
from backend.expense_service import (
    add_expense,
    get_user_expenses,
    get_monthly_expense_total
)
from backend.budget_service import (
    set_budget,
    get_monthly_budget,
    get_remaining_budget,
    generate_monthly_report
)

print("===== SMARTSPEND BACKEND TEST =====")

# 1. Register a new user
success, message = register_user(
    "Test User",
    "smartspend_test@example.com",
    "Test@12345"
)
print("\nRegistration:", message)

# 2. Login
success, result = login_user(
    "smartspend_test@example.com",
    "Test@12345"
)

if not success:
    print("Login failed:", result)
    raise SystemExit

user_id = result["user_id"]
print("Login successful!")
print("User ID:", user_id)

# 3. Add an expense
success, message = add_expense(
    user_id,
    500,
    "Food",
    "Lunch",
    "2026-11-10"
)
print("\nAdd expense:", message)

# 4. View expenses
expenses = get_user_expenses(user_id)
print("\nUser Expenses:", expenses)

# 5. Set monthly budget
success, message = set_budget(
    user_id, 11, 2026, 5000
)
print("\nSet budget:", message)

# 6. View monthly budget
budget = get_monthly_budget(user_id, 11, 2026)
print("Monthly budget:", budget)

# 7. Calculate expenses
total = get_monthly_expense_total(user_id, 11, 2026)
print("Total expenses:", total)

# 8. Calculate remaining budget
remaining, result = get_remaining_budget(
    user_id, 11, 2026
)
print("Remaining budget:", remaining)
print("Expense total:", result)

# 9. Generate monthly report
report = generate_monthly_report(user_id, 11, 2026)
print("\nMonthly Report:", report)

print("\n===== BACKEND TEST COMPLETED =====")

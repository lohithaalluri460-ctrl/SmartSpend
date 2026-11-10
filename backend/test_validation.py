
from backend.expense_service import add_expense

print("SMARTSPEND - VALIDATION TEST")

user_id = int(input("Enter your user ID: "))

# Test 1: Negative amount
print("\nTest 1: Negative amount")
print(add_expense(user_id, -500, "Food", "Lunch", "2026-11-10"))

# Test 2: Zero amount
print("\nTest 2: Zero amount")
print(add_expense(user_id, 0, "Food", "Lunch", "2026-11-10"))

# Test 3: Empty category
print("\nTest 3: Empty category")
print(add_expense(user_id, 500, "", "Lunch", "2026-11-10"))

# Test 4: Valid amount
print("\nTest 4: Valid amount")
print(add_expense(user_id, 500, "Food", "Lunch", "2026-11-10"))

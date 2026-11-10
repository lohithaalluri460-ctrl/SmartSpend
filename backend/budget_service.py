
from database.db_connection import get_connection



def set_budget(user_id, month, year, amount):

    if not isinstance(user_id, int) or user_id <= 0:
        return False, "Invalid user ID"

    try:
        month = int(month)
        year = int(year)
        amount = float(amount)
    except (ValueError, TypeError):
        return False, "Enter valid numeric values"

    if amount <= 0:
        return False, "Budget must be greater than zero"

    if month < 1 or month > 12:
        return False, "Invalid month"

    if year < 2000:
        return False, "Invalid year"

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT budget_id FROM budgets
            WHERE user_id = ? AND month = ? AND year = ?
        """, (user_id, month, year))

        existing_budget = cursor.fetchone()

        if existing_budget:
            cursor.execute("""
                UPDATE budgets SET amount = ?
                WHERE budget_id = ?
            """, (amount, existing_budget[0]))
        else:
            cursor.execute("""
                INSERT INTO budgets (user_id, month, year, amount)
                VALUES (?, ?, ?, ?)
            """, (user_id, month, year, amount))

        connection.commit()
        return True, "Budget saved successfully!"

    except Exception as e:
        connection.rollback()
        return False, str(e)

    finally:
        connection.close()


def get_monthly_budget(user_id, month, year):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
        SELECT amount
        FROM budgets
        WHERE user_id = ?
        AND month = ?
        AND year = ?
        """, (user_id, month, year))

        budget = cursor.fetchone()

        if budget is None:
            return None

        return budget[0]

    finally:
        connection.close()

from backend.expense_service import get_monthly_expense_total

def get_remaining_budget(user_id, month, year):
    budget = get_monthly_budget(user_id, month, year)

    if budget is None:
        return None, "No budget set for this month"

    total_expenses = get_monthly_expense_total(
        user_id, month, year
    )

    remaining = budget - total_expenses

    return remaining, total_expenses

from backend.expense_service import (
    get_monthly_expense_total,
    get_expense_summary_by_category
)

def generate_monthly_report(user_id, month, year):

    budget = get_monthly_budget(user_id, month, year)

    if budget is None:
        return None

    total_expenses = get_monthly_expense_total(
        user_id, month, year
    )

    remaining = budget - total_expenses

    category_summary = get_expense_summary_by_category(
        user_id, month, year
    )

    report = {
        "budget": budget,
        "total_expenses": total_expenses,
        "remaining": remaining,
        "category_summary": category_summary
    }

    return report


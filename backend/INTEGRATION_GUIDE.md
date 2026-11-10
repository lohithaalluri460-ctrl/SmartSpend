
# SmartSpend Backend Integration Guide

## 1. Authentication

Import:
from backend.auth import register_user, login_user

Registration:
register_user(name, email, password)

Login:
login_user(email, password)

## 2. Expense Management

Import:
from backend.expense_service import (
    add_expense,
    get_user_expenses,
    update_expense,
    delete_expense
)

## 3. Budget Management

Import:
from backend.budget_service import (
    set_budget,
    get_monthly_budget,
    get_remaining_budget,
    generate_monthly_report
)

## 4. Category Analytics

Import:
from backend.expense_service import (
    get_expense_summary_by_category
)

## 5. Database

All backend modules use the same SQLite database
through database/db_connection.py.

The frontend must call backend functions instead
of directly modifying database tables.

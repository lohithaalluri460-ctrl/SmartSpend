
import streamlit as st

from backend.auth import login_user
from backend.expense_service import get_user_expenses
from backend.budget_service import get_monthly_budget

st.title("SmartSpend - Integration Test")

st.subheader("Backend Connection")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    success, result = login_user(email, password)

    if success:
        st.session_state["user_id"] = result["user_id"]
        st.session_state["name"] = result["name"]
        st.success("Login successful!")
    else:
        st.error(result)

if "user_id" in st.session_state:
    user_id = st.session_state["user_id"]

    st.write("Welcome,", st.session_state["name"])

    expenses = get_user_expenses(user_id)

    st.subheader("Your Expenses")
    st.write(expenses)

    month = st.number_input(
        "Month", min_value=1, max_value=12, value=11
    )

    year = st.number_input(
        "Year", min_value=2000, max_value=2100, value=2026
    )

    budget = get_monthly_budget(
        user_id, int(month), int(year)
    )

    st.subheader("Your Monthly Budget")

    if budget is None:
        st.info("No budget set for this month.")
    else:
        st.metric("Monthly Budget", f"₹{budget:,.2f}")

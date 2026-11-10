

from database.db_connection import get_connection

def add_expense(user_id, amount, category, description, expense_date):

    # 1. Check user ID
    if not isinstance(user_id, int) or user_id <= 0:
        return False, "Invalid user ID"

    # 2. Check amount
    try:
        amount = float(amount)
    except (ValueError, TypeError):
        return False, "Amount must be a number"

    if amount <= 0:
        return False, "Amount must be greater than zero"

    # 3. Check category
    if not category or not category.strip():
        return False, "Category is required"

    # 4. Check expense date
    if not expense_date:
        return False, "Expense date is required"

    # 5. Store expense in database
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
        INSERT INTO expenses
        (user_id, amount, category, description, expense_date)
        VALUES (?, ?, ?, ?, ?)
        """, (user_id, amount, category.strip(), description, expense_date))

        connection.commit()
        return True, "Expense added successfully!"

    finally:
        connection.close()




def get_user_expenses(user_id):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute("""
        SELECT expense_id, amount, category,
               description, expense_date
        FROM expenses
        WHERE user_id = ?
        ORDER BY expense_date DESC
        """, (user_id,))

        expenses = cursor.fetchall()

        return expenses

    finally:
        connection.close()

def update_expense(
    expense_id,
    user_id,
    amount,
    category,
    description,
    expense_date
):

    if amount <= 0:
        return False, "Amount must be greater than zero"

    if not category.strip():
        return False, "Category is required"

    if not expense_date.strip():
        return False, "Expense date is required"

    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute("""
        UPDATE expenses
        SET amount = ?,
            category = ?,
            description = ?,
            expense_date = ?
        WHERE expense_id = ?
        AND user_id = ?
        """, (
            amount,
            category.strip(),
            description,
            expense_date,
            expense_id,
            user_id
        ))

        connection.commit()

        if cursor.rowcount == 0:
            return False, "Expense not found"

        return True, "Expense updated successfully!"

    finally:
        connection.close()

def delete_expense(expense_id, user_id):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute("""
        DELETE FROM expenses
        WHERE expense_id = ?
        AND user_id = ?
        """, (expense_id, user_id))

        connection.commit()

        if cursor.rowcount == 0:
            return False, "Expense not found"

        return True, "Expense deleted successfully!"

    finally:
        connection.close()


from database.db_connection import get_connection

def get_monthly_expense_total(user_id, month, year):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
        SELECT SUM(amount)
        FROM expenses
        WHERE user_id = ?
        AND strftime('%m', expense_date) = ?
        AND strftime('%Y', expense_date) = ?
        """, (user_id, f"{month:02d}", str(year)))

        result = cursor.fetchone()

        return result[0] if result[0] is not None else 0

    finally:
        connection.close()

def get_expense_summary_by_category(user_id, month, year):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        WHERE user_id = ?
        AND strftime('%m', expense_date) = ?
        AND strftime('%Y', expense_date) = ?
        GROUP BY category
        ORDER BY SUM(amount) DESC
        """, (user_id, f"{month:02d}", str(year)))

        return cursor.fetchall()

    finally:
        connection.close()

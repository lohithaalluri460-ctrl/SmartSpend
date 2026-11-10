
import sqlite3
import hashlib
import secrets

from database.db_connection import get_connection


# Function to securely hash password
def hash_password(password):

    salt = secrets.token_hex(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt.encode(),
        600000
    ).hex()

    return salt + ":" + password_hash


# Function to register a new user
def register_user(name, email, password):

    # Validate inputs
    name = name.strip()
    email = email.strip().lower()

    if not name or not email or not password:
        return False, "All fields are required"

    if "@" not in email or "." not in email:
        return False, "Invalid email address"

    if len(password) < 8:
        return False, "Password must contain at least 8 characters"

    # Hash password
    secure_password = hash_password(password)

    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute("""
        INSERT INTO users (name, email, password_hash)
        VALUES (?, ?, ?)
        """, (name, email, secure_password))

        connection.commit()

        return True, "Registration successful!"

    except sqlite3.IntegrityError:

        return False, "Email already registered"

    finally:
        connection.close()


import hmac


def verify_password(password, stored_hash):

    # Separate salt and original hash
    salt, original_hash = stored_hash.split(":", 1)

    # Hash the entered password using the same salt
    new_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt.encode(),
        600000
    ).hex()

    # Compare both hashes securely
    return hmac.compare_digest(new_hash, original_hash)

def login_user(email, password):

    email = email.strip().lower()

    if not email or not password:
        return False, "Email and password are required"

    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute("""
        SELECT user_id, name, password_hash
        FROM users
        WHERE email = ?
        """, (email,))

        user = cursor.fetchone()

        if user is None:
            return False, "Invalid email or password"

        user_id, name, stored_hash = user

        if verify_password(password, stored_hash):

            return True, {
                "user_id": user_id,
                "name": name
            }

        return False, "Invalid email or password"

    finally:
        connection.close()


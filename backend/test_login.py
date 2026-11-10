
from getpass import getpass

from backend.auth import login_user

print("SMARTSPEND LOGIN")

email = input("Enter your email: ")
password = getpass("Enter your password: ")

success, result = login_user(email, password)

if success:

    print("Login successful!")
    print("Welcome,", result["name"])
    print("User ID:", result["user_id"])

else:

    print(result)

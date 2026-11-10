
from getpass import getpass

from backend.auth import register_user

print("SMARTSPEND USER REGISTRATION")

name = input("Enter your name: ")
email = input("Enter your email: ")
password = getpass("Enter your password: ")

success, message = register_user(name, email, password)

print(message)

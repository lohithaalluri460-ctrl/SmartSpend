
import sqlite3
from pathlib import Path

# Get the database folder location
BASE_DIR = Path(__file__).resolve().parent

# Database file location
DB_PATH = BASE_DIR / "smartspend.db"

# Function to connect to database
def get_connection():

    connection = sqlite3.connect(DB_PATH)
    connection.execute("PRAGMA foreign_keys = ON")

    return connection

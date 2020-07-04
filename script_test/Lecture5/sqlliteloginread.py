import sqlite3
import os
from sys import exit
from hashlib import sha256
from getpass import getpass

DB_NAME = 'login.db'

def db_exists(db_name):
    if not os.path.exists(db_name):
        return False
    return True

if not db_exists(DB_NAME):
    print("Run this script where your login.db file was created")
    exit(1)

def validate_user():
    username = input("Username: ")
    password = getpass("Password: ")

    sha256_h = sha256()
    sha256_h.update(password.encode('utf-8'))
    digest = sha256_h.digest()

    conn = sqlite3.connect(DB_NAME)
    curs = conn.execute(f'SELECT username FROM users WHERE username="{username}" AND password="{digest}"')

    user = curs.fetchone()

    if not user:
        print("Invalid credentials")
    else:
        print(f"Welcome in {user[0]}!")

    conn.close()

validate_user()
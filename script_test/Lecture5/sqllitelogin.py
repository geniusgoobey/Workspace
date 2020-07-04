import sqlite3
import os
from random import choice
from hashlib import sha256
from string import ascii_letters, digits

DB_NAME = 'login.db'

if os.path.exists(DB_NAME):
    os.remove(DB_NAME)

def gen_password():
    alphabet = ascii_letters + digits
    return ''.join([choice(alphabet) for _ in range(30)]).encode('utf-8')

conn = sqlite3.connect(DB_NAME)

conn.execute('''
CREATE TABLE users (username text, password text)
''')

password = gen_password()

sha256_obj = sha256()
sha256_obj.update(password)
digest = sha256_obj.hexdigest()

conn.execute(f'INSERT INTO users VALUES ("admin", "{digest}")')
conn.commit()

conn.close()
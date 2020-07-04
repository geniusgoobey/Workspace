import sqlite3

DB_FILENAME = 'store.db'

conn = sqlite3.connect(DB_FILENAME)

conn.execute('''
CREATE TABLE customers (fname text, lname text, spent integer, last_on text)
''')

conn.execute('''
INSERT INTO customers VALUES ("Brian", "Rogers", 5015, "03/15/2019")
''')

conn.execute('''
INSERT INTO customers (spent, last_on, lname, fname) VALUES (1020, "11/09/2019", "Sidener", "Tom")
''')

conn.execute('''
INSERT INTO customers VALUES ("Lucinda", "Caughey", 10379, "06/03/2019")
''')

curs = conn.execute('''
SELECT * FROM customers
''')

for row in curs.fetchall():
    print(row)


    conn.execute('''
UPDATE customers SET spent=1237 WHERE fname="Tom"
''')

curs = conn.execute('''
SELECT * FROM customers
''')

for row in curs.fetchall():
    print(row)


    conn.execute('''
DELETE FROM customers WHERE lname="Rogers"
''')

curs = conn.execute('''
SELECT * FROM customers
''')

for row in curs.fetchall():
    print(row)

    conn.close()
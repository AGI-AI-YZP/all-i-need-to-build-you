import sqlite3

# Connect to a SQLite database
conn = sqlite3.connect('test.db')

# Create a cursor object
cur = conn.cursor()

# Create a table
cur.execute('''CREATE TABLE IF NOT EXISTS Employee
               (ID INT PRIMARY KEY     NOT NULL,
               NAME           TEXT    NOT NULL,
               AGE            INT     NOT NULL);''')

# Insert data into the table
cur.execute("INSERT INTO Employee (ID, NAME, AGE) VALUES (1, 'John', 30);")

# Commit the changes and close the connection
conn.commit()
conn.close()
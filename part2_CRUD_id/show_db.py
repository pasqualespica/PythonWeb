import sqlite3

conn = sqlite3.connect('people.db')
cur = conn.cursor()
cur.execute('SELECT * FROM person ORDER BY lname')
people = cur.fetchall()
print(type(people))
print(people)
print("--------")
for person in people:
    print(f'{person[2]} {person[1]}')

import sqlite3

connect = sqlite3.connect('cars.sqlite')
cursor = connect.cursor()

cursor.execute("""
CREATE table if not exists cars (
    id integer primary key,
    name text,
    color text,
    number integer
);
""")

cursor.execute("insert into cars values (0, 'mercedes', 'black', 12345)")
cursor.execute("insert into cars values (1, 'ferrari', 'red', 12346)")
cursor.execute("insert into cars values (2, 'lamborgini', 'yellow', 12347)")
cursor.execute("insert into cars values (3, 'bmw', 'white', 12348)")
cursor.execute("insert into cars values (4, 'lada', 'brown', 12349)")

connect.commit()
cursor.execute("SELECT * FROM cars")
results = cursor.fetchall()
print(results)

connect.close()

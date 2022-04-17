import sqlite3

connect = sqlite3.connect('cars.sqlite')
cursor = connect.cursor()

cursor.execute("""SELECT * FROM cars
                    UNION
""")
print(cursor.fetchall())

connect.close()
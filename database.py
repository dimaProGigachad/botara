import sqlite3

connect = sqlite3.connect('cars.sqlite')
cursor = connect.cursor()

cursor.execute("""
    SELECT cars.number,cars.color,owners.owner,models.mark
    FROM cars,owners,models
    WHERE cars.id_owner=owners.id and cars.id_model=models.id
    """)
print(cursor.fetchall())    

cursor.execute("insert into owners values (4, 'Игорь', '122')")
cursor.execute("insert into owners values (5, 'Виктор', '121')")
cursor.execute("insert into owners values (6, 'Андрей', '125')")
cursor.execute("insert into owners values (7, 'Андрей', '126')")
cursor.execute("insert into owners values (8, 'Ира', '124')")

cursor.execute("insert into models values (4, 'Chevrolet', 'Camaro', 'USA' )")
cursor.execute("insert into models values (5, 'Chevrolet', 'Camaro', 'USA' )")
cursor.execute("insert into models values (6, 'Lexus', 'RX', 'Japan' )")
cursor.execute("insert into models values (7, 'Lada', 'Kalina', 'Russia' )")
cursor.execute("insert into models values (8, 'Daewoo', 'Matiz', 'South Korea' )")

cursor.execute("insert into cars values (4, '134', 'yellow', '998','111')")
cursor.execute("insert into cars values (5, '777', 'black', '228','222')")
cursor.execute("insert into cars values (6, '324', 'gray', '334','333')")
cursor.execute("insert into cars values (7, '333', 'brown', '112','444')")
cursor.execute("insert into cars values (8, '432', 'green', '009','555')")
connect.commit()

connect.close()

import sqlite3

# connection = sqlite3.connect('section12/test_data.db')
connection = sqlite3.connect(':memory:')

cursor = connection.cursor()

cursor.execute(
    'CREATE TABLE IF NOT EXISTS persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
)

insert_sql = 'INSERT INTO persons(name) values(?)'
cursor.execute(insert_sql, ('Mike',))
cursor.execute(insert_sql, ('Nancy',))
cursor.execute(insert_sql, ('Jun',))
connection.commit()

cursor.execute('UPDATE persons set name = "Michel" WHERE name = "Mike"')
connection.commit()

cursor.execute('DELETE FROM persons WHERE name = "Jun"')
connection.commit()

cursor.execute('SELECT * FROM persons')
for row in cursor:
    print(row)

cursor.close()
connection.close()

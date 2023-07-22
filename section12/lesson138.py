import mysql.connector

connection = mysql.connector.connect("localhost", "root", "password", "xxxxxxxx")
cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS test_database")
cursor.execute("USE test_database")
cursor.execute("CREATE TABLE IF NOT EXISTS persons(id int NOT NULL AUTO_INCREMENT PRIMARY KEY, name STRING)")

insert_sql = 'INSERT INTO persons(name) values(%s)'
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

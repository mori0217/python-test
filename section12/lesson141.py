import time
import sqlite3
import memcache

db = memcache.Client(["127.0.0.1:11211"])

db.set("web_page", "value1", time=3)
print(db.get("web_page"))
time.sleep(3)
print(db.get("web_page"))

db.set("counter", 0)
db.incr("counter", 1)
db.incr("counter", 1)
db.incr("counter", 1)
print(db.get("counter"))


connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.execute("CREATE TABLE persons (id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)")
cursor.execute("INSERT INTO persons(name) values('Mike')")


def get_id(name):
    id = db.get(name)
    if id:
        return id
    cursor.execute("SELECT * FROM persons WHERE name = ?", (name,))
    person = cursor.fetchone()
    if not person:
        raise Exception("No person")
    id, name = person
    db.set(name, id, time=60)
    return id


print(get_id("Mike"))
print(get_id("Nancy"))
print(get_id("Mike"))

connection.commit()
connection.close()

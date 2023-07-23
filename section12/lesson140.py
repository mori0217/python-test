import dbm

with dbm.open("section12/cache", "c") as db:
    db["key1"] = "value1"
    db["key2"] = "value2"

with dbm.open("section12/cache", "r") as db:
    print(db.get("key1"))

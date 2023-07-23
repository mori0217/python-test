from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))


def clear_db(tx):
    tx.run("MATCH (n) DETACH DELETE n")


def add_friend(tx, name, friend_name=None):
    if not friend_name:
        return tx.run("CREATE (p:Person {name: $name}) "
                      "RETURN p", name=name)
    return tx.run("MATCH (p:Person {name: $name}) "
                  "create (p)-[:FRIEND]->(:Person {name: $friend_name}) ",
                  name=name, friend_name=friend_name)


def print_friend(tx, name):
    for record in tx.run("MATCH (p:Person {name: $name})-[:FRIEND]->(yourFriend) "
                         "RETURN yourFriend.name", name=name):
        print(record["yourFriend.name"])


with driver.session() as session:
    session.write_transaction(clear_db)
    session.write_transaction(add_friend, "Alice")
    for f in ["Bob", "Carol", "Dave"]:
        session.write_transaction(add_friend, "Alice", f)
    session.read_transaction(print_friend, "Alice")

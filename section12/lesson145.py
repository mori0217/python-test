from bson import ObjectId
from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)
db = client['test_database']

stack1 = {
    'name': 'customer1',
    'pip': ['python', 'java', 'go'],
    'info': {'os': 'mac'},
    "date": datetime.datetime.utcnow()
}

stack2 = {
    'name': 'customer2',
    'pip': ['python', 'java'],
    'info': {'os': 'windows'},
    "date": datetime.datetime.utcnow()
}

db_stacks = db.stacks
stack_id1: ObjectId = db_stacks.insert_one(stack1).inserted_id
stack_id2: ObjectId = db_stacks.insert_one(stack2).inserted_id

print(stack_id1)
print(stack_id2)

print(db_stacks.find_one({'_id': stack_id1}))
print(db_stacks.find_one({'_id': stack_id2}))

for stack in db_stacks.find():
    print(stack)

now = datetime.datetime.utcnow()
for stack in db_stacks.find({"date": {"$lt": now}}):
    print(stack)
for stack in db_stacks.find({"date": {"$gte": now}}):
    print(stack)

db_stacks.find_one_and_update(
    {"name": "customer1"}, {"$set": {"name": "customerX"}}
)
print(db_stacks.find_one({"name": "customerX"}))

db_stacks.delete_one({"name": "customerX"})
print(db_stacks.find_one({"name": "customerX"}))

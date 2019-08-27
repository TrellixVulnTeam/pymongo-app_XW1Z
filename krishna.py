import pymongo

mongoclient = pymongo.MongoClient("mongodb://localhost:27017/")
# new_db = mongoclient["krishdb"];
# print(mongoclient.list_database_names())

krishdb = mongoclient["krishdb"]
krishcollection = krishdb["users"]
user1 = { "name":"ganesh", "age":100, "state":"Vrindavan", "city":"UP", "hobby":"cricket", "interest":"reading" }
# status = krishcollection.insert_one(user1)
# if(status):
#     print("inserted id - ", status.inserted_id)
# else:
#     print("not inserted")
for item in krishcollection.find({ "name" : { "$regex":"^k" } }):
    print(item)

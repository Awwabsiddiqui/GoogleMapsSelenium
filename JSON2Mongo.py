import json

import pymongo

def JSON2Mongo(jsnData):
    client = pymongo.MongoClient(
        "mongodb+srv://devlopmentEnvUser:7fnRQHco54caq5EA@cluster0-mgfdf.gcp.mongodb.net/?retryWrites=true&w=majority")
    db = client['netclandev']
    collection = db['usersDummyB']
    collection.insert_one(jsnData)

# with open('merchant2.json') as file:
#     file_data = json.load(file)
#     JSON2Mongo(file_data)


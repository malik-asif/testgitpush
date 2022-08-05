import pymongo
client = pymongo.MongoClient("mongodb+srv://malikasif:Mongo687@cluster0.cg7lrlo.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d ={
    'name': 'asif',
    'email': 'malikasif@xyz.com',
    'surname': 'malik'
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
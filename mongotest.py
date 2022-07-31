import pymongo

client = pymongo.MongoClient("mongodb+srv://PankajKewat:mongodb123@cluster0.z8usz.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name": "pankajkewat",
    "email" :"pankaj@gmail.com",
    "surname": "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

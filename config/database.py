from pymongo import MongoClient


client = MongoClient("mongodb+srv://saravanangs:Saravanan2608@keepclone.tmzd9vg.mongodb.net/?retryWrites=true&w=majority")
db = client.todo_db
collection_name = db ["todo_collection"]
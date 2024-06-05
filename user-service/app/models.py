import pymongo
from app.config import settings


# Establish a connection to your MongoDB server
client = pymongo.MongoClient(settings.DB_URL)

# Access your database
db = client[settings.DB_NAME]

# Define your collection (similar to a table in SQL)
user_collection = db["users"] 

def get_user(user_id):
    user = user_collection.find_one({"_id": user_id})
    return user

def create_user(user_data):
    user_id = user_collection.insert_one(user_data).inserted_id
    return get_user(user_id)

def update_user(user_id, updated_data):
    user_collection.update_one({"_id": user_id}, {"$set": updated_data})
    return get_user(user_id)

def delete_user(user_id):
    user_collection.delete_one({"_id": user_id})

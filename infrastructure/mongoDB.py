import pymongo
from dotenv import load_dotenv
import os

import pymongo.asynchronous

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = pymongo.MongoClient(MONGO_URI)
db = client["otp-verify"]
collection = db["otp"]

collection.create_index([("email", pymongo.ASCENDING)], unique=True)
collection.create_index([("name")])
collection.create_index([("orders")])
collection.create_index([("created_at")])
collection.create_index([("updated_at")])
collection.create_index([("liked")])

collection.create_index([("timestamp", pymongo.ASCENDING)], expireAfterSeconds=300)
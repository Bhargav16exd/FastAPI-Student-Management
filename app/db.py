from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("DATABASE_URL")


def initiate_database():
    print("hi")
    client = MongoClient(url)
    db =  client["student_database"]
    print(db)
    collection = db["students"]
    return collection

collection = initiate_database()



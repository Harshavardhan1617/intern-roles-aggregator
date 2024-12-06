from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["internships_data"]
internship_collection = db["internships"]
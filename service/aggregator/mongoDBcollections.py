from pymongo import MongoClient, errors

try:
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)

    client.admin.command("ping")
    print("Connected to MongoDB successfully!")
    
    db = client["internships_data"]
    internship_collection = db["internships"]

except errors.ConnectionFailure as e:
    print(f"Failed to connect to MongoDB: {e}")
except errors.ServerSelectionTimeoutError as e:
    print(f"MongoDB server selection timed out: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

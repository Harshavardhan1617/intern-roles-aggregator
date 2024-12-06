def MongoLoader(dataObject, collection): 
    try:
        result = collection.insert_many(dataObject, ordered=False)
        print("data saved to collections")
        print(result.inserted_ids)
    except Exception as e:
        print(f"following error occured while inserting data {e}")
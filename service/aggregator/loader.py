from pymongo.errors import BulkWriteError

def MongoLoader(dataObject, collection):
    print("Starting to load data...")
    try:
        # Attempt to insert data
        result = collection.insert_many(dataObject, ordered=False)
        print(f"Data saved to collection successfully. {len(result.inserted_ids)} documents inserted.")
    except BulkWriteError as bwe:
        # Calculate duplicates and inserted documents
        write_errors = bwe.details.get("writeErrors", [])
        duplicate_count = sum(1 for error in write_errors if error.get("code") == 11000)  # Duplicate key error code
        total_errors = len(write_errors)
        total_inserted = len(dataObject) - total_errors

        # Display a summary of the error
        print(f"Batch operation completed with errors:")
        print(f"  - {total_inserted} documents inserted.")
        print(f"  - {duplicate_count} duplicate documents found.")
        print(f"  - {total_errors - duplicate_count} other errors occurred.")

        for error in write_errors:
            print(f"Error: {error.get('errmsg')}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

import links

from pymongo import MongoClient

from service.aggregator.scrapers.internshala_scraper import scraper
client = MongoClient("mongodb://localhost:27017/")
db = client["internships_data"]
internship_collection = db["internships"]

url = links.internshala_url

def main():
   dataObject =  scraper(url)
   try:
        result = internship_collection.insert_many(dataObject, ordered=False)
        print("data saved to collections")
        print(result.inserted_ids)
   except Exception :
        print("duplicates were found and skipped insertion")

        
if __name__ == "__main__":
    print("this is main function")
    main()
import links
from service.aggregator.scrapers.internshala_scraper import scraper
from service.aggregator.loader import MongoLoader
from service.aggregator.collections import internship_collection


url = links.internshala_url

def main():
   dataObject =  scraper(url) #extract and transform
   MongoLoader(dataObject=dataObject, collection=internship_collection) #load the data by passing result dictionary and db collection name

        
if __name__ == "__main__":
    print("this is main function")
    main()
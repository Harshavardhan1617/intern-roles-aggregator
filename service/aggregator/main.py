import links

import requests
from bs4 import BeautifulSoup

from scrapers.internshala_scraper import scraper
from loader import MongoLoader
from mongoDBcollections import internship_collection



url = links.internshala_url

def main():
      
      try:       
         response = requests.get(url)
         response.raise_for_status()

         soup = BeautifulSoup(response.content, "lxml")
         print("parsed the html")
      except requests.RequestException as e:
         print(f"An error occurred: {e}") #extract

      dataObject =  scraper(soup) #transform
      MongoLoader(dataObject=dataObject, collection=internship_collection) #load the data by passing result dictionary and db collection name

        
if __name__ == "__main__":
    print("this is main function")
    main()
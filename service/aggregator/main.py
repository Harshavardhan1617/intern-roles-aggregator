import links
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["internships_data"]
internship_collection = db["internships"]

url = links.internshala_url

def scraper(url):

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "lxml")
        print("parsed the html")

        internships = soup.find_all("div", class_=["container-fluid", "individual_internship"])

        count = 0
        grouped_data = []
        for internship in internships:
            internship_id = internship.get("internshipid")
            if not internship_id:
                continue

            company_name = internship.find("p", class_="company-name").get_text(strip=True)
            job_link_tag = internship.find("a", class_="job-title-href")
            job_title = job_link_tag.get_text(strip=True)
            job_link = job_link_tag.get("href")
            actively_hiring = internship.find("div", class_="actively-hiring-badge") is not None
            row1_items = internship.find_all("div", class_="row-1-item")
            location = row1_items[0].get_text(strip=True) if len(row1_items) > 0 else "N/A"
            duration = row1_items[1].get_text(strip=True) if len(row1_items) > 1 else "N/A"
            stipend = row1_items[2].get_text(strip=True) if len(row1_items) > 2 else "N/A"

            grouped_data.append({
                "_id": internship_id,
                "company_name": company_name,
                "job_title": job_title,
                "job_link": f"https://internshala.com{job_link}",
                "actively_hiring": actively_hiring,
                "location": location,
                "duration": duration,
                "stipend": stipend,
            })
            count +=1
            print(f"scraped {count} internships from internshala")
        return grouped_data

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []



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
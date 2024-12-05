import links
import requests
from bs4 import BeautifulSoup
url = links.internshala_url

def scraper(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "lxml")

    internships = soup.find_all("div", class_=["container-fluid", "individual_internship"])

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
            "internship_id": internship_id,
            "company_name": company_name,
            "job_title": job_title,
            "job_link": f"https://internshala.com{job_link}",
            "actively_hiring": actively_hiring,
            "location": location,
            "duration": duration,
            "stipend": stipend,
        })

    print(grouped_data[0])

def main():
    scraper(url)

if __name__ == "__main__":
    print("this is main function")
    main()
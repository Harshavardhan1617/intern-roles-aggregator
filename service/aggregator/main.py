import links
import requests
from lxml import html
from bs4 import BeautifulSoup

url = links.internshala_url

try:
    response = requests.get(url)
    response.raise_for_status()  

    soup = BeautifulSoup(response.content, "lxml")

    internships = soup.find_all("div", class_=["container-fluid", "individual_internship"])

    data = []
    if internships: 
        for internship in internships:
            internship_id = internship.get("internshipid", "N/A")
            data.append(internship_id)
        print(data)


except requests.RequestException as e:
    print(f"An error occurred while fetching the page: {e}")
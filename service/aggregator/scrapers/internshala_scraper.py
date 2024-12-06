def scraper(soup):
    try:
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

    except :
        print("Error while transforming soup")
        return []
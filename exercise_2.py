import requests
from bs4 import BeautifulSoup
import json

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extrahera jobbdata
jobs = []
job_elements = soup.find_all("div", class_="card-content")
for job_elem in job_elements:
    title = job_elem.find("h2", class_="title").text.strip()
    company = job_elem.find("h3", class_="company").text.strip()
    location = job_elem.find("p", class_="location").text.strip().title()  # Första bokstaven versal
    date_posted = job_elem.find("time").text.strip()
    
    jobs.append({
        "title": title,
        "company": company,
        "location": location,
        "date_posted": date_posted
    })

# Spara till JSON
with open("job_search_v2.json", "w", encoding="utf-8") as file:
    json.dump(jobs, file, ensure_ascii=False, indent=4)

import requests
from fastapi import FastAPI
from bs4 import BeautifulSoup



app=FastAPI()

#initialize and test fastapi
@app.get("/")
def read_root():
    return {"message":"Hello, use /scrape to initiate scraping"}

def scrape_website(url):
    response = requests.get(url)
    if response.status_code ==200:
        soup = BeautifulSoup(response.content,"lxml")
        enrollment = soup.find('th',text="Enrollment")
        enrollment_num = enrollment.find_next('td').get_text(strip=True)
        print("Enrollment: ",enrollment_num[0:3])
        print("Max Capacity: ",enrollment_num[13:16])
        

        return response.content
    else:
        return{"error":"requests.get failed"}


#get a scraping root
@app.get("/scrape")
def scrape():
    url = "http://www.columbia.edu/cu/bulletin/uwb/subj/COMS/W4995-20233-001/"
    scraped_data = scrape_website(url)
    print(url)
    return scraped_data



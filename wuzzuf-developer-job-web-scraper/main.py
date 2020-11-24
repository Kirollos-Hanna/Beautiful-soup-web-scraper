from bs4 import BeautifulSoup
import requests

htmlText = requests.get(
    'https://wuzzuf.net/a/Remote-Junior-Web-Developer-Jobs-in-Egypt?start=0&filters%5Bcareer_level%5D%5B0%5D=Entry%20Level&filters%5Broles%5D%5B0%5D=IT%2FSoftware%20Development&filters%5Bcountry%5D%5B0%5D=Egypt').text

soup = BeautifulSoup(htmlText, 'lxml')
jobs = soup.find_all('div', class_="result-wrp row")
for job in jobs:
    companyNameHTML = job.find(
        'span', class_='company-name').span
    companyName = "Confidential"
    if(companyNameHTML):
        companyName = companyNameHTML.text
    jobDetailsArray = job.find(
        'div', class_="job-details").text.replace(" ", "").split()
    jobDetails = "".join(jobDetailsArray)
    moreInfo = job.find("h2", class_="job-title").a['href']
    print(moreInfo)
    print(f'''
    Company Name: {companyName}
    Job Details: {jobDetails}
    More Info: {moreInfo}
    ''')
    print("")

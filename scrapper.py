from bs4 import BeautifulSoup
import requests

link = "https://www.linkedin.com/jobs/search?keywords=Backend&location=israel&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
f = requests.get(link)
data = f.text
with open("home.html","w") as f :
        f.write(data)



soup=BeautifulSoup(data,'lxml')

jobs=soup.find_all('div',class_='base-search-card__info')
for j in jobs:
    position=j.h3.text.strip()
    company = j.h4.a.text.strip()
    print(position,"-",company)
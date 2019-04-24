from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
driver.implicitly_wait(3)

def ImageDownload(url, filename):
    with open(filename, "wb") as f:
        resp = get(url)
        f.write(resp.content)

url = 'http://www.megabox.co.kr/?menuId=movie-boxoffice'

driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

bo = soup.find('div', {'class':'movie_container'}).find_all('img')

rank = 1
for i in bo:
    title = i.get('alt')
    imglink = i.get('src')

    ImageDownload(imglink, str(rank) + "위 " + title + ".jpg")

    if rank == 10:
        exit()

    rank += 1
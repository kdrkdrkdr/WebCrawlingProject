from bs4 import BeautifulSoup
from selenium import webdriver

# 멜론 차트 크롤링

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
driver.implicitly_wait(3)

url = "https://www.melon.com/chart/index.htm"

driver.get(url)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

melon_chart = soup.find('div', {'class':'service_list_song type02 d_song_list'}).find_all("div", {"class":"ellipsis rank01"})

rank = 0
for mc in melon_chart:

    if rank == 0:
        print("맟춤추천 : " + mc.text.strip())
    else:
        print(str(rank) + "위 " + mc.text.strip())
    rank += 1

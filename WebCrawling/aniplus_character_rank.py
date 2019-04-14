from bs4 import BeautifulSoup
from selenium import webdriver

# 애니 플러스 캐릭터 순위 크롤링

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
driver.implicitly_wait(3)

url = "http://www.aniplustv.com/#/ranking/characterRank.asp"

driver.get(url)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

today_character_rank = soup.select('div[class=nmw]')

rank = 1
print()
for trank in today_character_rank:
    print(str(rank) + "위 " + trank.text.strip())
    rank += 1

driver.quit()

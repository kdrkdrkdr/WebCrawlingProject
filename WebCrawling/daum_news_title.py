from bs4 import BeautifulSoup
from requests import get

# 다음 뉴스 제목 크롤링

url = "https://media.daum.net/ranking/popular/"

html = get(url).text

soup = BeautifulSoup(html, 'html.parser')

newslist = soup.find_all('strong', {"class":"tit_thumb"})

for news in newslist:
    print(news.text)
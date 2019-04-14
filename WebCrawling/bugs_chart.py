from requests import get
from bs4 import BeautifulSoup

# 우리나라 기준 벅스 차트 1~100위 크롤링

url = "https://music.bugs.co.kr/chart/track/realtime/total?nation=KR"

html = get(url).text

soup = BeautifulSoup(html, 'html.parser')

chart = soup.find_all("p", {"class":"title"})

rank = 1
for rank_list in chart:
    print(str(rank) + "위 " + rank_list.text.strip(), end='')
    print()
    rank += 1
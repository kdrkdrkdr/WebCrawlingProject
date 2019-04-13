from requests import get
from bs4 import BeautifulSoup

# 1위부터 100위까지 크롤링

url = "https://myanimelist.net/topanime.php"

html = get(url).text
soup = BeautifulSoup(html, 'html.parser')

rank_list = soup.find("div", {"class":"pb12"}).find_all("a", {"class":"hoverinfo_trigger fl-l fs14 fw-b"})

rank_num = 1
for rank in rank_list:
    print(str(rank_num) + ". " + rank.text)
    rank_num += 1
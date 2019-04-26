from bs4 import BeautifulSoup
from requests import get

url = str(input('불법-유해 정보 사이트 주소를 입력하세요. :'))
soup = BeautifulSoup(get(url).content, 'html.parser')
tag = soup.find_all('meta')

realUrl = tag[1].get('content').replace("0;url=", "").replace("'", "")
realSoup = BeautifulSoup(get(realUrl).content, 'html.parser')

info = realSoup.find_all('td')
for i in info:
    print(i.text)
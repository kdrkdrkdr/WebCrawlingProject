from requests import get
from bs4 import BeautifulSoup
GetSoup = lambda url_addr: BeautifulSoup(get(url_addr, headers={'User-agent' : 'Mozilla/5.0'}).text, 'html.parser')
lawNum = int(input('대한민국 제 몇조를 찾아보실건가요? : '))
lawFormat = '제{}조'.format(lawNum)
tempSoup = GetSoup("http://law.go.kr/법령/대한민국헌법/제{}조".format(lawNum))
realSoup = GetSoup("http://law.go.kr" + tempSoup.iframe['src'])
lawContent = realSoup.find('div', {'class':'lawcon'}).find_all('p')
for l in lawContent:
    print(l.text, '\n')
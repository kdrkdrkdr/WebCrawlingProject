from bs4 import BeautifulSoup
from requests import get, exceptions
from os import getcwd, mkdir, chdir
from shutil import rmtree

GetSoup = lambda url_addr: BeautifulSoup(get(url_addr, headers=header).text, 'html.parser', from_encoding='cp949')

header = {'User-agent' : 'Mozilla/5.0'}
baseURL = "https://ncode.syosetu.com"

soup = GetSoup(str(input('ダウンロードする小説アドレスを入力してください。: ')))

bigTitle = soup.find('p', {'class':'novel_title'}).text
index = soup.find('div', {'class':'index_box'}).find_all('dl')

try:
    mkdir('{}'.format(bigTitle))

except FileExistsError:
    rmtree('{}'.format(bigTitle), ignore_errors=True)
    mkdir('{}'.format(bigTitle))

finally:
    chdir('{}'.format(bigTitle))

count = 0
for i in index:
    nURL = baseURL + i.find('a')['href']
    nTitle = i.find('a').text

    nSoup = GetSoup(nURL)
    nContent = nSoup.find('div', {'id':'novel_honbun'}).find_all('p')

    novelContent = ""
    for nC in nContent:
        novelContent += str(nC.text) + "\n"

    count += 1
    with open('{}_{}.txt'.format(count, nTitle), 'w', encoding="utf-8") as f:
        f.write(novelContent)

chdir('../')
print('ダウンロード完了です。')
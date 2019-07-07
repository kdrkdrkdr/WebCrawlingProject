from bs4 import BeautifulSoup
from requests import get
from os import getcwd

url = "https://free-proxy-list.net/"
html = get(url).text
soup = BeautifulSoup(html, 'html.parser')

proxyAddr = soup.find("tbody").find_all('tr')
contents = ""

for i in proxyAddr:
    j = i.find_all('td')

    for k in j:
        content = k.text + ","
        contents += content

    contents += "\n"

with open('proxylist.csv', 'w') as f:
    f.write('IP Address,Port,Code,Country,Anonymity,Google,Https,Last Checked\n\n')
    f.write(contents)

print("[{}\\proxylist.csv] 에 저장되었습니다.".format(getcwd()))
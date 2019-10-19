from urllib.request import urlretrieve, urlopen
from bs4 import BeautifulSoup as bs

u = str(input('xhamster video url >> '))
a = bs(urlopen(u).read(), 'html.parser')
b = a.select_one('body > div.main-wrap > main > div.width-wrap.with-player-container > div.player-container > a')
c = b['href']
t = a.h1.text
urlretrieve(url=c, filename='{}.mp4'.format(t))
print("Download complete!")
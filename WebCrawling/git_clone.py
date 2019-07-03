# git clone 웹 크롤링으로 구현

from bs4 import BeautifulSoup
from requests_html import HTMLSession
from sys import argv
from requests import get
from zipfile import ZipFile
from os import remove
from os import rename

def download(filename, url):
    try:
        with open(filename, "wb") as f:
            resp = get(url)
            f.write(resp.content)
    except ConnectionError:
        pass

def unzip(filename, destination):
    with ZipFile(filename, 'r') as zf:
        zf.extractall(path=destination)
        zf.close()

if argv[1] == "clone":

    hSession = HTMLSession()
    
    html = hSession.get(argv[2]).text

    soup = BeautifulSoup(html, 'html.parser')
    gitloc = soup.find("div", {"class":"mt-2"}).find_all("a")

    baseurl = "https://github.com"

    href1 = gitloc[1].get('href')

    git = baseurl + href1

    href2 = href1.split("/")[2]

    fname = href2 + ".zip"

    download(fname, git)

    unzip(fname, "./")

    rename(href2 + "-master", href2)

    remove(fname)

    

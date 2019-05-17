from bs4 import BeautifulSoup
from selenium import webdriver
from requests import get
from time import sleep
from os import getcwd, mkdir, chdir
from os.path import isdir

def download(filename, url):
    try:
        with open(filename, "wb") as f:
            resp = get(url)
            f.write(resp.content)
    except ConnectionError:
        pass

# Chrome Webdriver
#=====================================================================
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
driver.implicitly_wait(3)
#=====================================================================

def InstaImgDownloader():

    username = str(input('Input Username that want to download photos : '))

    url = "https://www.instagram.com/{}".format(username) + "/"
    driver.get(url)
    hyperText = driver.page_source
    soupObj = BeautifulSoup(hyperText, 'html.parser')

    try:
        instaImg = soupObj.find('article', {'class':'FyNDV'}).find_all('img')

        directoryName = 'Instagram - ' + username

        count = 1

        lastHeight = driver.execute_script("return document.body.scrollHeight")

        while True:

            for img in instaImg:
                imgLink = img.get('src')

                if isdir('./{}'.format(directoryName)) == True:
                    pass
                else:
                    mkdir(directoryName)

                chdir(directoryName)

                download('{0}{1}.jpg'.format(username, count), imgLink)

                chdir('../')
                count += 1

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(3)

            newHeight = driver.execute_script("return document.body.scrollHeight")


            if newHeight == lastHeight:
                break

            lastHeight = newHeight
        

    except AttributeError:
        print('해당 유저 아이디가 존재하지 않습니다.')
        

if __name__ == "__main__":
    InstaImgDownloader()
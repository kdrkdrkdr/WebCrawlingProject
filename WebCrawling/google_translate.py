from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
driver.implicitly_wait(3)

word = str(input('모르는 단어나 문장을 입력해주세요. : '))

if word.replace(" ", "") != "":

    google_url = 'https://translate.google.co.kr/#view=home&op=translate&sl=auto&tl=ko&text={}'.format(word)

    driver.get(google_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    google_translate = soup.find('span', {'class':'tlid-translation translation'})
    print("뜻(구글 번역) : " + google_translate.text + "\n")
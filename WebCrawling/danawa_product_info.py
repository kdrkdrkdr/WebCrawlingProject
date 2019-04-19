#-*-coding:utf-8-*-

# 다나와 상품 정보 크롤링

from bs4 import BeautifulSoup
from selenium import webdriver

def printInfo(String1="", List=[], String2=""):
    for lst in List:
        print("\n" + String1 + lst.text + String2)

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--silent')
driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
driver.implicitly_wait(3)

url = str(input("\n다나와 상품 url을 넣어주세요. : "))

if not 'prod.danawa.com' in url:
    print("\n다나와 상품 주소가 아닙니다.")
    exit(0)

driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

danawa_pName        = soup.select('#blog_content > div.summary_info > div.top_summary > h3')
danawa_pDesc        = soup.select('#blog_content > div.summary_info > div.top_summary > div > div.sub_dsc > p')
danawa_pKeyword     = soup.select('#blog_content > div.summary_info > div.top_summary > div > div.sub_dsc > div > dl > dd > div > div')
danawa_lowest       = soup.select('#blog_content > div.summary_info > div.detail_summary > div.summary_left > div.lowest_area > div.lowest_list > table > tbody.high_list > tr.lowest > td.price > a > span.txt_prc > em')
danawa_reg_day      = soup.select('#thumbArea > div.made_info > div > span:nth-child(1)')
danawa_reg_company  = soup.select('#makerTxtArea > a')

printInfo(String1="상품이름: ", List=danawa_pName)
printInfo(String1="설명: ", List=danawa_pDesc)
printInfo(String1="키워드: ", List=danawa_pKeyword)
printInfo(String1="최저가: ", List=danawa_lowest, String2="원")
printInfo(List=danawa_reg_day)
printInfo(String1="제조사: ", List=danawa_reg_company)

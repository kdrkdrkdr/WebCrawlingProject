from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver

# 네이버 실시간 급상승 검색어 크롤링

while True:

    try:
        print("\n0) 전체 연령대\n1) 10대\n2) 20대\n3) 30대\n4) 40대\n5) 50대\n6) 프로그램 종료\n")
        agegroup = int(input("연령대를 입력하세요. : "))

        if agegroup in [0, 1, 2, 3, 4, 5, 6]:
            
            if agegroup == 0: age = "all"
            if agegroup == 1: age = "10s"
            if agegroup == 2: age = "20s"
            if agegroup == 3: age = "30s"
            if agegroup == 4: age = "40s"
            if agegroup == 5: age == "50s"
            if agegroup == 6: print("\n프로그램을 종료합니다."); break

            options = webdriver.ChromeOptions()
            options.add_argument('headless')

            driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
            driver.implicitly_wait(3)

            url = "https://datalab.naver.com/keyword/realtimeList.naver?where=main"

            driver.get(url)

            html = driver.page_source

            soup = BeautifulSoup(html, 'html.parser')

            rank = 1

            realtime_rank = soup.find('div', {"data-age":age}).find_all('span', {"class":"title"})

            for rank_all in realtime_rank:
                print(str(rank) + "위 " + rank_all.text)
                rank += 1

        else:
            print('\n연령대를 다시 선택해주세요.')

    except ValueError:
        print("\n연령대를 다시 선택해주세요.")
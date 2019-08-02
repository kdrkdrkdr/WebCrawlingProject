# 셀레늄 임포트
from selenium import webdriver

# 맞춤법 검사기 url
url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=맞춤법+검사기"

# 드라이버 로드
driver = webdriver.Chrome('chromedriver.exe')

# 암묵적 3초 기다리기
driver.implicitly_wait(3)

# url에서 정보 로드하기
driver.get(url)

# 검사할 맞춤법 입력
driver.find_element_by_xpath('//*[@id="tfGrammar"]').send_keys('검사 할 맞춤법')

# 검사하기 버튼 클릭
driver.find_element_by_xpath('//*[@id="btnGrammarCheck"]').click()

# 검사된 맞춤법 출력
print(driver.find_element_by_xpath('//*[@id="contResult"]').text)

# 드라이버 닫기
driver.close()

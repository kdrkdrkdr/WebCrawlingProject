# 네이버 블로그 글 자동화

from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')

driver.implicitly_wait(3)

naverLoginUrl = "https://nid.naver.com/nidlogin.login"

driver.get(naverLoginUrl)


naverLoginId = ""
naverLoginPw = ""


driver.find_element_by_name('id').send_keys(naverLoginId)

driver.find_element_by_name('pw').send_keys(naverLoginPw)

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()



naverBlogWriteUrl = "https://blog.naver.com/{}?Redirect=Write".format(naverLoginId)

driver.get(naverBlogWriteUrl)

driver.implicitly_wait(3)

title = ""

contents = """
"""

driver.find_element_by_xpath('//*[@id="SE-ce7714a0-95c0-416a-8b6a-c671161fbbd3"]').send_keys(title)

driver.find_element_by_xpath('//*[@id="SE-4d66bd03-9aeb-4e7a-9c17-968b540e3926"]/span[2]').send_keys(contents)

driver.close()
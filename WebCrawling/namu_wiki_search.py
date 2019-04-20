from bs4 import BeautifulSoup
from requests import get

keyword = str(input('\n나무위키에서 찾을 검색어를 입력하세요. : '))
page    = int(input('\n몇쪽까지 찾아볼까요? : '))

base_url   = "https://namu.wiki"
search_url = base_url + "/search/"
count = 0

for p in range(0, page, 1):
    print("\n" + str(p+1) + " 페이지")
    print('{}\n'.format('='*30))

    url = search_url + keyword + "?page={}".format(p+1)

    html = get(url).content
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    titles = soup.find('section', {'class':'search-section'}).find_all('a')

    for link in titles:
        check = link.get('href').find('/w/')

        if check == 0:
            print("제목 : " + link.text.strip())
            print("링크 : " + base_url + link.get('href') + "\n")
            count += 1
    page += 1

print("\n[총 {}개의 검색결과가 나왔습니다.]".format(count))
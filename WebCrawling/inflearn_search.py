from bs4 import BeautifulSoup
from requests import get


def inflearnSearch():


    sq = str(input("인프런에서 검색할 강좌 이름을 입력해주세요. : "))

    lst = []
    page = 1
    count = 1
    pgcount = 2

    while True:

        baseUrl = "https://www.inflearn.com"
        url = "https://www.inflearn.com/courses?order=search&s={0}&page={1}".format(sq, page)

        html = get(url).content
        soup = BeautifulSoup(html, 'html.parser')

        titles = soup.findAll("div", {"class":"course_title"})
        prices = soup.findAll("div", {"class":"price has-text-right column is-half"})
        links = soup.findAll("a", {"class":"course_card_front"})
        instructor = soup.findAll("div", {"class":"instructor has-text-right column is-half"})
        students = soup.findAll("div", {"class":"student_num column is-half"})
        stars = soup.findAll("div", {"class":"star_solid"})

        for i in range(0, len(titles), 1):
            check = titles[i].get_text().strip()

            if check in lst:
                pgcount -= 1
                break
            lst.append(check)

            print(count)
            print("강좌 : {0}".format(titles[i].get_text().strip()))
            print("가격 : {0}".format(prices[i].get_text().strip()))
            print("링크 : {0}{1}".format(baseUrl, links[i].get("href").strip()))
            print("진행자 : {0}".format(instructor[i].get_text().strip()))
            print("학생 수 : {0}".format(students[i].get_text().strip()))
            print("평점 : {0}".format(str(round((float((stars[i].get("style").strip().replace("width: ", "").replace("%", "")))/20), 1)) + "/5.0개"))
            print("\n")
            
            count += 1

        page += 1
        
        if pgcount == 0:
            break

if __name__ == "__main__":
    inflearnSearch()
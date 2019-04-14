from bs4 import BeautifulSoup
from requests import get
from sys import argv, stdout

# Ani24 기준 편성표 입니다.

class Ani24(object):

    def __init__(self):
        self.rank  = 1
        self.url   = ""
        self.page  = 1


    def daylist(self, num):
        print()

        dayoftheweek = ['월', '화', '수', '목', '금', '토', '일']

        if num in [1, 2, 3, 4, 5, 6, 7]:
            print("[{}요일] 편성표 입니다.".format(dayoftheweek[num-1]))
        else:
            pass

        print()

        self.url = "https://ani24video.com/ani/search.php?type=%i" %num
        html = get(self.url).text
        soup = BeautifulSoup(html, 'html.parser')
        ani_name  = soup.find("div", {"class":"ani_search_list_box"}).find_all("a", {"class":"subject"})

        for link in ani_name:
            print("-------------------------------------------------")
            print("제목 : " + link.get('title'))
            print("링크 : " + "https://ani24video.com" + link.get('href'))
        print("-------------------------------------------------")
        return
    
    def newtop20(self):
        self.url = "https://ani24video.com/ani/top10.html"
        html = get(self.url).text
        soup = BeautifulSoup(html, 'html.parser')
        newtop_list = soup.find("div", {"class":"ani_list_top_center"}).find_all("div", {"class":"subject"})

        print()
        for link in newtop_list:
            print(str(self.rank) + "위 " + link.text)
            self.rank += 1

        return


    def genretop20(self, genre):
        self.url = "https://ani24video.com/ani/top10.html?type=genre&genre={0}".format(genre)
        html = get(self.url).text
        soup = BeautifulSoup(html, 'html.parser')
        genretop_list = soup.find("div", {"class":"ani_list_top_center"}).find_all("div", {"class":"subject"})

        for link in genretop_list:
            print(str(self.rank) + "위 " + link.text.strip())
            self.rank += 1

        return

        

    def quartertop20(self, year, quarter):

        self.url = "https://ani24video.com/ani/top10.html?type=quarter&year={0}&quarter={1}".format(str(year), str(quarter))
        html = get(self.url).text
        soup = BeautifulSoup(html, 'html.parser')
        quartertop_list = soup.find("div", {"class":"ani_list_top_center"}).find_all("div", {"class":"subject"})

        for link in quartertop_list:
            print(str(self.rank) + "위 " + link.text)
            self.rank += 1

        return
        

    def yeartop20(self, year):
        
        self.url = "https://ani24video.com/ani/top10.html?type=year&year={0}".format(str(year))

        html = get(self.url).text

        soup = BeautifulSoup(html, 'html.parser')

        yeartop_list = soup.find("div", {"class":"ani_list_top_center"}).find_all("div", {"class":"subject"})

        for link in yeartop_list:
            print(str(self.rank) + "위 " + link.text)
            self.rank += 1

        return

    def completedlist(self, page=1, genre="all", producer="all"):

        self.url = "https://ani24video.com/ani/search.php?type=all&page={0}&order=new&genre={1}&producer={2}".format(str(page), str(genre), str(producer))
        
        html = get(self.url).text

        soup = BeautifulSoup(html, 'html.parser')

        completed_list = soup.find("div", {"class":"ani_search_list_box"}).find_all("a", {"class":"subject"})
        

        for link in completed_list:
            print(link.get('title'))

        return




if __name__ == "__main__":

    genrelist = ['로맨스', '드라마', '판타지', '먼치킨', '멘붕', '공포', '공포', '능력', '코미디', '학원', '하렘', 'BL', '부활동', '마법', 'SF', '전쟁', 
                 '군', '메카닉', '액션', '퇴마', '유령', '귀신', '요괴', '이세계', '여동생', '미스테리', '스포츠', '범죄', '정령', '뱀파이어', '아이돌']

    while True:

        select = int(input('\n1) 요일별 편성표'
                           '\n2) 신작-Top20'
                           '\n3) 장르-Top20'
                           '\n4) 분기-Top20'
                           '\n5) 올해-Top20'
                           '\n6) 완결-Top'
                           '\n7) 프로그램 종료'
                           '\n\n옵션을 선택하세요. : '))

        if select == 1:

            while True:

                try:
                    day = int(input('\n1) 월요일'
                                    '\n2) 화요일'
                                    '\n3) 수요일'
                                    '\n4) 목요일'
                                    '\n5) 금요일'
                                    '\n6) 토요일'
                                    '\n7) 일요일'
                                    '\n8) 뒤로 가기'
                                    '\n\n요일을 선택하세요. : '))
                    if day in [1, 2, 3, 4, 5, 6, 7]:
                        Ani24().daylist(day)
                    elif day == 8:
                        break
                    else:
                        print("요일을 다시 선택해주세요.\n")
                    
                except ValueError:
                    print("요일을 다시 선택해주세요.\n")

        elif select == 2:
            Ani24().newtop20()

        elif select == 3:
            print(len(genrelist))
            print("장르 리스트 : " + ', '.join(genrelist))
            genre = str(input("장르를 입력해주세요. : "))
            genre_name = genre.replace(" ", "")
            if genre_name in genrelist:
                Ani24().genretop20(genre_name)
            else:
                print("장르를 다시 선택해주세요.\n")
                



        elif select == 4:
            try:
                year    = int(input("연도를 입력하세요. : "))
                quarter = int(input("분기를 입력하세요. : "))
                Ani24().quartertop20(year, quarter)
            except ValueError:
                print("다시 입력해주세요.\n")

        elif select == 5:
            try:
                year = int(input("연도를 입력하세요. : "))
                Ani24().yeartop20(year)
            except ValueError:
                print("연도를 다시 입력해주세요.\n")


        elif select == 6:
            try:
                page  = int(input("페이지를 입력하세요.")) 
                genre = str(input("장르를 입력하세요."))


            except ValueError:
                pass


        elif select == 7:
            break

        else:
            print("옵션을 다시 선택해주세요.\n")
        
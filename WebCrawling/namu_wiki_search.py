from bs4 import BeautifulSoup
from requests import get
from os import name, system, getcwd
from pdfcrowd import HtmlToPdfClient

base_url   = "https://namu.wiki"
    

def MakePdfFile(docUrl, fname):
    client = HtmlToPdfClient('kdrhacker', '9d78eaf477a691680fe410fb664e59f6')
    client.convertUrlToFile(docUrl, fname)

def ClearWindow():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def Banner():
    banner = '''
                                             _ __   _ 
    ____  ____ _____ ___  __  __   _      __(_) /__(_)
   / __ \/ __ `/ __ `__ \/ / / /  | | /| / / / //_/ / 
  / / / / /_/ / / / / / / /_/ /   | |/ |/ / / ,< / /  
 /_/ /_/\__,_/_/ /_/ /_/\__,_/    |__/|__/_/_/|_/_/   
             나무위키 검색 엔진 by kdr
                                                        
    '''
    print(banner)

def Search():
    ClearWindow()
    try:
        keyword = str(input('\n나무위키에서 찾을 문서를 입력하세요. : '))
        page    = int(input('몇쪽까지 찾아볼까요? : '))
        search_url = base_url + "/search/"
        count = 0
        Banner()

        for p in range(0, page, 1):
            print("\n\n" + str(p+1) + " 페이지")
            print('{}\n'.format('='*len(str(p+1) + " 페이지")*2))

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

        print("\n\n총 {}개의 결과가 검색되었습니다.".format(count))
    
    except (ValueError, EOFError, KeyboardInterrupt):
            print("\n다시 선택해주세요.\n")


def Document():
    ClearWindow()
    try:
        title = str(input("문서 제목을 입력해주세요. : "))
        Banner()
        w_url = base_url + "/w/" + title

        if title.replace(" ", "") != "":
            filename = '{} - 나무위키.pdf'.format(title)
            MakePdfFile(w_url, filename)
            print("[{}\\{}] 에 '{}' 문서가 저장되었습니다.".format(getcwd(), filename, title))

    except (ValueError, EOFError, KeyboardInterrupt):
        print("\n다시 입력해주세요.\n")



def main():
    ClearWindow()
    Banner()
    while True:
        try:
            select = int(input("\n1) 문서 제목 찾기\n2) 문서 다운로드 하기\n3) 프로그램 종료\n\n옵션을 선택해주세요. : "))
            if select == 1:
                Search()
            elif select == 2:
                Document()
            elif select == 3:
                ClearWindow()
                break
            else:
                print("\n다시 선택해주세요.\n")

        except (ValueError, EOFError, KeyboardInterrupt):
            print("\n다시 선택해주세요.\n")


if __name__ == "__main__":
    main()

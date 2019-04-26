from bs4 import BeautifulSoup
from requests import get
from os import name, system, mkdir, path, chdir, getcwd
from shutil import rmtree

base_url   = "https://namu.wiki"
    

def Download(url, filename):
    with open(filename, "wb") as f:
        resp = get(url)
        f.write(resp.content)

def FileWrite(filename, *lst):
    f = open(filename, 'w', encoding='utf-8')
    for i in lst:
        f.write(i.text + "\n")
    f.close()

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
        keyword = str(input('\n나무위키에서 찾을 검색어를 입력하세요. : '))
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
    
    except ValueError:
            print("\n다시 선택해주세요.\n")

    except EOFError:
        print("\n다시 선택해주세요.\n")


def Document():
    ClearWindow()
    try:
        title = str(input("문서 제목을 입력해주세요. : "))
        Banner()
        w_url = base_url + "/w/" + title
        html = get(w_url).content
        soup = BeautifulSoup(html, 'html.parser')

        if title.replace(" ", "") != "":

            wiki_document_title     = soup.find_all('span', {'class':'wiki-document-title'})
            wiki_edit_day           = soup.find_all('p', {'class':'wiki-edit-date'})
            wiki_category           = soup.find_all('div', {'class':'wiki-category'})
            wiki_toc_item           = soup.find_all('span', {'class':'toc-item'})
            wiki_heading            = soup.find_all('h2', {'class':'wiki-heading'})
            wiki_paragraph          = soup.find_all('div', {'class':'wiki-paragraph'})
            wiki_footnote_list      = soup.find_all('span', {'class':'footnote-list'})
            wiki_image              = soup.find_all('img', {'class':'wiki-image'})

            for h in wiki_heading:
                print(h.text + "\n" + "="*100)
                for p in wiki_paragraph:
                    print(p.text)

            for title in wiki_document_title:
                dir_name = str(title.text) + '(namu.wiki)'

            if '/' in dir_name:
                dir_name = dir_name.replace('/', ' ')

            if path.exists(dir_name) == True:
                rmtree('./{}'.format(dir_name), ignore_errors=True)
                    
            mkdir("{}".format(dir_name))

            chdir("./{}".format(dir_name))

            fname = dir_name + " (문서).txt"

            FileWrite(fname, 
                *wiki_document_title,
                *wiki_edit_day,
                *wiki_category,
                *wiki_toc_item,
                *wiki_heading,
                *wiki_paragraph,
                *wiki_footnote_list)

            img_count = 0
            for img in wiki_image:
                check = img.get('src')
                for fname in wiki_document_title:
                    if '//w.namu.la' in check:
                        w_img_url = "https:" + check
                        Download(w_img_url, '{}'.format(str(fname.text) + str(img_count + 1) + ".jpg").replace('/', ' '))
                        img_count += 1
            chdir('../')
            
            print("[" + getcwd() + "\\" + dir_name + "]" + " 에 나무위키 문서가 저장되었습니다.")

    except KeyboardInterrupt:
        print("\n다시 입력해주세요.\n")

Document()

def main():
    ClearWindow()
    Banner()
    while True:
        try:
            select = int(input("\n1) 검색어로 찾기\n2) 문서로 찾기\n3) 프로그램 종료\n\n옵션을 선택해주세요. : "))
            if select == 1:
                Search()
            elif select == 2:
                Document()
            elif select == 3:
                ClearWindow()
                break
            else:
                print("\n다시 선택해주세요.\n")

        except ValueError:
            print("\n다시 선택해주세요.\n")

        except EOFError:
            print("\n다시 선택해주세요.\n")

if __name__ == "__main__":
    main()

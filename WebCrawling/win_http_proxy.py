# 이 프로그램은 WebCrawlingProject/get_proxy_address.py 를 변형 한것입니다.
# 사용자가 프록시 설정을 랜덤으로 바꿀수 있으며, 자동적으로 바뀌게 할 수 있습니다.

from bs4 import BeautifulSoup
from requests import get, exceptions
from os import getcwd, system
from random import choice
from ctypes import windll
from time import sleep

ProxyList = []
selectList = '''
1. 프록시 리스트 저장하기
2. 프록시 확인하기
3. 프록시 적용하기
4. 프록시 초기화
5. 프록시 서비스로 실행하기
6. 프로그램 종료

>> '''

def checkInternetConnection():
    try:
        response = get("https://www.google.com")
        return True
    except ( exceptions.ConnectionError ):
        return False
    

def echooff():
    system('echo off')
    return
    

def showProxy():
    system('netsh winhttp show proxy')


def applyProxy(ip_port="", reset=False):
    if ip_port.replace(' ', '') != "":
        system('netsh winhttp set proxy {}'.format(ip_port))

    if reset == True:
        system('netsh winhttp reset proxy')

    return


def getProxy(Store=False):
    url = "https://free-proxy-list.net/"
    html = get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    proxyAddr = soup.find("tbody").find_all('tr')
    contents = ""

    for i in proxyAddr:
        j = i.find_all('td')

        ip = j[0].text
        port = j[1].text
        ProxyList.append("{}:{}".format(ip, port))


        for k in j:
            content = k.text + ","
            contents += content

        contents += "\n"
    
    if Store == False:
        return

    else:
        with open('{}\\proxylist.csv'.format(getcwd()), 'w') as f:
            f.write('IP Address,Port,Code,Country,Anonymity,Google,Https,Last Checked\n\n')
            f.write(contents)

        print("[{}\\proxylist.csv] 에 저장되었습니다.".format(getcwd()))
    return


def apply():
    echooff()
    getProxy(Store=False)
    proxy = choice(ProxyList)
    applyProxy(ip_port=proxy)


def serviceProxy():
    while True:
        try:
            print("\n[Ctrl-C 를 입력하면 종료됩니다.]\n")
            apply()        
            sleep(60)
            system("cls")
        except ( KeyboardInterrupt ):
            break

def main():

    if checkInternetConnection() == False:
        exit('인터넷 연결을 확인하세요.')


    if windll.shell32.IsUserAnAdmin() == True:

        while True:

            try:
                select = int(input(selectList))

                if select == 1:
                    getProxy(Store=True)

                elif select == 2:
                    showProxy()

                elif select == 3:
                    apply()              
                
                elif select == 4:
                    applyProxy(reset=True)


                elif select == 5:
                    serviceProxy()


                elif select == 6:
                    exit("프로그램을 종료합니다.")

                else:
                    print("다시 선택해주세요.\n")

            except ( ValueError, KeyboardInterrupt, EOFError ):
                print("다시 선택해주세요.\n")

    else:
        exit("관리자 권한으로 실행시켜주세요.")


if __name__ == "__main__":
    main()

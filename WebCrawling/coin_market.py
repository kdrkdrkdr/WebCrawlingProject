from bs4 import BeautifulSoup
from requests_html import HTMLSession
from csv import writer


hSession = HTMLSession()
hParser = "html.parser"


coinUrl = "https://coinmarketcap.com/all/views/all/"
coinHtml = hSession.get(coinUrl).text
coinSoup = BeautifulSoup(coinHtml, hParser)


coinCsv = open('coinlist.csv', 'w', encoding='utf-8', newline='')
coinWriter = writer(coinCsv)
coinWriter.writerow(['#', 'Name', 'Symbol', '$ Market Cap', '$ Price', '$ Circulating Supply', '$ Volume (24h)', '% 1 hour', '% 24 hours', '% 7 days'])


coinList = coinSoup.find('table', {'id':'currencies-all'}).find('tbody').find_all('tr')

for coin in coinList:

    coinProperty =  coin.find_all('td')

    coinNumber = coinProperty[0].text
    coinName = coinProperty[1].get('data-sort')
    coinSymbol = coinProperty[2].text
    coinMarketCap = coinProperty[3].text.replace('$', '').replace('\n', '')
    coinPrice = coinProperty[4].text.replace('$', '')
    coinCirculatingSupply = coinProperty[5].text.replace('\n', '').replace('*', '')
    coinVolume24h = coinProperty[6].text.replace('$', '').replace('\n', '')
    coinPercent1h = coinProperty[7].text.replace('%', '')
    coinPercent24h = coinProperty[8].text.replace('%', '')   
    coinPercent7d = coinProperty[9].text.replace('%', '')


    coinListBar = [coinNumber, coinName, coinSymbol, coinMarketCap, coinPrice, coinCirculatingSupply, coinVolume24h, coinPercent1h, coinPercent24h, coinPercent7d]

    coinWriter.writerow(coinListBar)

coinCsv.close()

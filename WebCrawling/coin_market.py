from bs4 import BeautifulSoup
from requests_html import HTMLSession
from csv import writer
from time import sleep, strftime
from pandas import read_csv
from matplotlib import pyplot
from numpy import arange


filename = '{}__coinlist.csv'.format(strftime("%Y-%m-%d__%H-%M-%S"))


def main(showGraph=False):
    global filename

    hSession = HTMLSession()
    hParser = "html.parser"

    coinUrl = "https://coinmarketcap.com/all/views/all/"
    coinHtml = hSession.get(coinUrl).text
    coinSoup = BeautifulSoup(coinHtml, hParser)

    coinCsv = open(filename, 'w', encoding='utf-8', newline='')
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


    if showGraph == True:
        coinCsv = read_csv(filename)

        number = coinCsv['#']
        name = coinCsv['Name']
        symbol = coinCsv['Symbol']
        marketCap = coinCsv['$ Market Cap']
        price = coinCsv['$ Price']
        circulatingSupply = coinCsv['$ Circulating Supply']
        volume24h = coinCsv['$ Volume (24h)']
        percent1h = coinCsv['% 1 hour']
        percent24h = coinCsv['% 24 hours']
        percent7d = coinCsv['% 7 days']


        xValue = list(symbol[0:10])
        yValue = list(percent1h[0:10])
        nGroups = len(xValue)
        index = arange(nGroups)

        pyplot.plot(xValue, yValue, 'r.--')

        pyplot.xlim(-1, nGroups)
        pyplot.ylim(-2, 2)

        pyplot.xlabel('Coin Type')
        pyplot.ylabel('Rate of change in 1 hour')


        pyplot.show()


if __name__ == "__main__":
    # If you want only store csv file, main(showGraph=False)
    main(showGraph=True)

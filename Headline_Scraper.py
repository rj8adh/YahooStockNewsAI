# ToDo: implement ai and ask if title is enough info, if not, go to URL and look at the related stock and first paragraph

import bs4
import requests

url='https://finance.yahoo.com/quote/'
stocks = []

stock = input("What stocks do you want to webscrape?(type end to quit) ")
stocks.append(stock.upper())

while stocks[-1].lower() != 'end':
    stock = input("What stocks do you want to webscrape?(type end to quit) ")
    stocks.append(stock.upper())

for i in range(len(stocks) - 1):
    print('*********************************************************\n\n' + stocks[i], '\n\n*********************************************************')
    soup = bs4.BeautifulSoup(requests.get(url + stocks[i] + '/').text, 'html.parser')
    
    # print(soup)
    
    anchor = soup.find_all('a', attrs={'class':'subtle-link fin-size-small thumb yf-1e4diqp'})
    
    for atrb in anchor:
        print('Title: ', atrb['title'])
        print('URL: ', atrb['href'])
        if atrb != anchor[-1]:
            print('-------------------')
    
    
    # print(anchor)


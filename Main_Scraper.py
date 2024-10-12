# TODO: implement ai and ask if title is enough info, if not, go to URL and look at the related stock and first paragraph

def scrapeInfo(printOut=False, selenium_scrape=False):
    from Specific_Scraper import scrapeDetail
    import bs4
    import requests
    from openai import OpenAI
    import os
    from Selenium_Scraper_Prototype import seleniumScrape

    client = OpenAI(api_key=os.getenv("API_KEY"))


    url='https://finance.yahoo.com/quote/'

    stocks = []

    all_info = []
    all_titles = []
    all_links = []

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
            
            if printOut:
                print('Title: ', atrb['title'])
                print('URL: ', atrb['href'])

            article_info = scrapeDetail(atrb['href'])

            # check if there is any easy to access html on the page
            if article_info:
                all_info.append(article_info)
                all_titles.append(atrb['title'])
                all_links.append(atrb['href'])

                if printOut:
                    print(article_info)

            elif selenium_scrape:
                print("SELENIUEEFIMEFIMEFIMIMIMI", seleniumScrape(atrb['href']))

            if atrb != anchor[-1]:
                if printOut:
                    print('-------------------')
    return all_info, all_titles, all_links
        
        # print(anchor)

scrapeInfo(True, True)
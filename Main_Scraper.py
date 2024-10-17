# TODO: implement ai and ask if title is enough info, if not, go to URL and look at the related stock and first paragraph

def scrapeInfo(printOut=False, selenium_scrape=False, compareRelatedStocks=False):
    from Specific_Scraper import scrapeDetail
    import bs4
    import requests
    from openai import OpenAI
    import os
    from Selenium_Scraper_Prototype import seleniumScrape

    client = OpenAI(api_key=os.getenv("API_KEY"))


    url='https://finance.yahoo.com/quote/'

    # full info will contain multiple all infos
    full_info = []
    stocks = []
    all_titles = []
    all_links = []



    stock = input("What stocks do you want to webscrape?(type end to quit) ")
    stocks.append(stock.upper())

    while stocks[-1].lower() != 'end':
        stock = input("What stocks do you want to webscrape?(type end to quit) ")
        stocks.append(stock.upper())

    # loops the same amount of times there are stocks(-1 for the end call)
    for i in range(len(stocks) - 1):

        # all info is for all the info on a specific stock
        all_info = []
        stock_titles = []
        url = url + stocks[i]

        print('*'*20 + '\n\n' + stocks[i], '\n\n' + '*'*20)
        # Get info from base stock--where we get headlines and urls
        soup = bs4.BeautifulSoup(requests.get(url).text, 'html.parser')
        
        # print(soup)
        
        anchor = soup.find_all('a', attrs={'class':'subtle-link fin-size-small thumb yf-1e4diqp'})
        
        # for headline in the anchor
        for atrb in anchor:

            containsRelated = False

            if not compareRelatedStocks:

                if printOut:
                    print('Title: ', atrb['title'])
                    print('URL: ', atrb['href'])

                if not compareRelatedStocks:
                    article_info, relatedStocks = scrapeDetail(atrb['href'])     

                    # check if scrapeDetail returned something, if not use selenium scraper
                    if article_info:
                        all_info.append(article_info)
                        stock_titles.append(atrb['title'])
                        all_links.append(atrb['href'])

                        if printOut:
                            print(article_info)

                    # check if we are supposed to selenium scrape
                    elif selenium_scrape:

                        seleniumDesc, relatedStocks = seleniumScrape(atrb['href'])

                        if printOut:
                            print("Selenium Scraped:", seleniumDesc)

                        all_info.append(seleniumDesc)
                        stock_titles.append(atrb['title'])
                        all_links.append(atrb['href'])                
       
            else:
                # Ok, Ill admit, this is a bit lazy, not defining a function
                seleniumDesc, relatedStocks = seleniumScrape(atrb['href'])

                if printOut:
                    # print("Selenium Scraped:", seleniumDesc)
                    print('\n\nTitle: ', atrb['title'])
                    print('URL: ', atrb['href'])

                all_info.append(seleniumDesc)
                stock_titles.append(atrb['title'])
                all_links.append(atrb['href'])

                # Loop through every stock tagged in the article
                for relatedStock in relatedStocks:
                    print('\n\nRELATED STOCK', relatedStock)
                    # Check if the related stock is the one you are asking for
                    if relatedStock == stocks[i]:
                        containsRelated = True
                        print('RELATED')
                        break

                    else:
                        containsRelated = False
                        print('USELESS :/')

                if not containsRelated:
                    all_info.pop()
                    stock_titles.pop()
                    all_links.pop()


            if atrb != anchor[-1]:
                if printOut:
                    print("-"*30)


        # compile each stocks specifics into a nested list
        full_info.append(all_info)
        all_titles.append(stock_titles)

    return full_info, all_titles, all_links, stocks
        
        # print(anchor)

# x, y, z, stock = scrapeInfo(printOut=True, compareRelatedStocks=True)
# print(y)
def scrapeDetail(url):

    import bs4
    import requests

    soup = bs4.BeautifulSoup(requests.get(url).content, 'html.parser')
    # print(soup)

    output = ''
    related_stocks = []

    # get all the paragraph stuff
    page_info = soup.select('p')

    # delete the bottom portion of the article to get rid of extra irrelevant stuff
    del page_info[len(page_info)//3:]

    # loop through paragraph item
    for info in page_info:

        # check for ads and remove from output
        if ':' in info.getText():
            continue

        output+=info.getText() + ' '
        
    # print(output)

    # hugging face sentiment analysis has max of 512 tokens or around 2500 characters
    if len(output) > 2000:
        output = output[0:1999]
    return output, related_stocks

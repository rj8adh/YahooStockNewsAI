# ToDo: implement ai and ask if title is enough info, if not, go to URL and look at the related stock and first paragraph

def scrapeDetail(url, headline=''):

    import bs4
    import requests

    soup = bs4.BeautifulSoup(requests.get(url).content, 'html.parser')
    output = ''

    # print(soup)

    # get all the paragraph stuff
    page_info = soup.select('p')

    # only get 1/3rd of the info
    del page_info[:len(page_info)//3]

    # loop through paragraph item
    for info in page_info:

        # check for ads and remove from output
        if ':' in info.getText():
            continue

        output+=info.getText() + ' '
    print(output)

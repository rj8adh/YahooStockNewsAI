# ToDo: implement ai and ask if title is enough info, if not, go to URL and look at the related stock and first paragraph

import bs4
import requests

url='https://finance.yahoo.com/news/iphone-losing-buzz-among-teens-170828608.html'
stocks = []

soup = bs4.BeautifulSoup(requests.get(url).content, 'html.parser')

# print(soup)

page_info = soup.select('p')

del page_info[len(page_info)//3:]

for info in page_info:
    if ':' in info.getText():
        continue
    print(info.getText())







#------------------------------------------------------------------------------------------#




# url='https://finance.yahoo.com/news/billionaires-deciding-sell-shares-well-114500994.html'
# stocks = []

# soup = bs4.BeautifulSoup(requests.get(url).content, 'html.parser')

# # anchor = soup.select("p")

# page_info = soup.find_all('p')

# for info in page_info:

#     print(info.getText())


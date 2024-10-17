# TODO: Get rid of the annoying News • thing that gets printed



def seleniumScrape(url):

    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    import bs4
    from selenium.webdriver.chrome.options import Options

    # import json

    all_info = ""
    raw_stocks = []
    related_stocks = []
    
    # Increase performance by not loading images and stuff
    options = Options()
    options.add_argument("--blink-settings=imagesEnabled=false")
    # options.add_argument("--headless=new")

    # Configure a chrome webdriver with our defined options
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    # driver.get(url)

    # content = driver.find_elements(By.CLASS_NAME, 'body yf-5ef8bf')

    content = driver.page_source

    driver.quit()

    # content = content.replace(",", "\n")

    soup = bs4.BeautifulSoup(content, 'html.parser')
    elements_with_class = soup.select('p', attrs={'class' : 'yf-1pe5jgt'})
    raw_stocks = [element.text for element in soup.find_all(class_="ticker medium hover2 border streaming extraPadding yf-138ga19")]

    print("RAW STOCKS:", raw_stocks)

    # Takes the raw stock information and turns it into a list of just the stock names
    for stock in raw_stocks:
        split_stocks = stock.split('   ')
        split_stocks.pop()
        split_stocks = split_stocks[0].split(' ')
        related_stocks.append(split_stocks[1])

    # print(related_stocks)

    # stuff I dont want in the output(junk)
    matches = ["•", "Try again.", "Tip:", "Sign in to access your portfolio"]



    for element in elements_with_class:
        # check if element is empty
        if element.getText():
            # check to see if element is junk
            if any(x in element.getText() for x in matches):
                continue
            all_info += element.getText() + ' '
    
    # Hugging Face has 520 token limit
    if len(all_info) > 1000:
        all_info = all_info[0:999]

    return all_info, related_stocks

    # with open("Results.json", mode="w") as write_file:
    #     json.dump(content, write_file)

# info, stock = seleniumScrape('https://finance.yahoo.com/news/prediction-meta-platforms-worth-more-115300124.html')
# print(stock)

"""
TEST LINKS:
https://finance.yahoo.com/video/cpi-data-nvidia-stock-surge-174449597.html
https://finance.yahoo.com/video/jpmorgan-earnings-fedspeak-ppi-data-213045517.html
https://finance.yahoo.com/m/7ba4c6e9-e00c-3c14-a4f5-caaf8dfbc5b9/tesla-stock-is-down-this.html
https://finance.yahoo.com/m/ae39fcf1-66a3-3b58-a5ed-89a19dcf8f92/these-stocks-moved-the-most.html
https://finance.yahoo.com/m/cd237eb1-8d14-3db1-8769-e8facc2639da/tesla-stock-closes-lower.html
https://finance.yahoo.com/video/why-investor-skeptical-teslas-robotaxi-212201481.html
https://finance.yahoo.com/video/jpmorgan-earnings-fedspeak-ppi-data-213045517.html
"""
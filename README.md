# Yahoo Stock News AI

This program scrapes various Yahoo News articles on given stock tickers and returns the news sentiment on that topic.

## Description

This program utilizes the requests library to scrape still pages, and selenium to scrape dynamic pages. For most efficient runtime, don't run selenium as there are a very limited number of dynamic articles on Yahoo, and using selenium greatly slows down the system. Additionally, the script uses a HuggingFace sentiment analysis model to assess the article.

## Getting Started

### Installing
```
pip install -r requirements.txt
```
* Ensure all dependencies are installed and up to date

### Executing program

* Run the program by running Sentiment_Analysis.py

## Help

If requirements aren't updated, or you run into any conflicts with newer versions, please let me know

## Authors

Contributors names and contact info

Aarjit Adhikari
[@rj8](microrew0@gmail.com)

## Version History

* 1.1
    * Various bug fixes and optimizations
* 1.0
    * Initial Release

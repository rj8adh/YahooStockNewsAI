# Yahoo Stock News AI

This program scrapes various Yahoo News articles on given stock tickers and returns the news sentiment on that topic.

## Description

This program utilizes the requests library to scrape still pages, and selenium to scrape dynamic pages. For most efficient runtime, don't run selenium as there are a very limited number of dynamic articles on Yahoo, and using selenium greatly slows down the system. Additionally, the script uses a HuggingFace sentiment analysis model to assess the article.

## Getting Started

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

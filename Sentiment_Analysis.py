from fastapi import FastAPI
from transformers import pipeline
from Main_Scraper import scrapeInfo

# used to figure out what stocks info we are on
counter = 0

pipe = pipeline("text-classification", model="mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")

app = FastAPI()

data, title, links, stock_order = scrapeInfo(compareRelatedStocks=True)

stock_sentiments = []

# loops through every stock we asked for
for stock in data:
    # Reset positive and negative counter
    positives = 0
    negatives = 0

    print("\n\nSTOCK:", stock, "\n\n")
    print(f'\n\n\n{stock_order[counter]}\n\n\n')

    # loops through every stocks individual news articles
    for i in range(len(stock)):

        # print(title[i])
        # print(links[i])
        # print(data[i])

        # get transformer result for data
        outputs = pipe(stock[i], top_k=None) # top_k=None just makes it so I get all the percentage results, not just the highest

        # If the transformer returns the highest label as neutral, get the second highest label
        if outputs[0]['label'] == 'neutral':

            print('Low Confidence Title Was:', title[counter][i])
            print('Neutral or:', outputs[1]['label'])

            if outputs[1]['label'] == 'positive':
                positives += 1

            else:
                negatives += 1

        else:
            print('High Confidence Title Was:', title[counter][i])
            print(outputs[0]['label'])

            if outputs[0]['label'] == 'positive':
                positives += 1

            else:
                negatives += 1
    
    stock_sentiments.append([positives, negatives])

    print('NUMBER OF POSITIVE TITLES:', positives)
    print('NUMBER OF NEGATIVE TITLES:', negatives)

    counter += 1

# Print the number of stocks with positive and negative at end of program
for i in range(len(stock)-1):
    print("\n\n", "-" * 50)
    print(stock_order[i], "had", stock_sentiments[i][0], "positive articles, and", stock_sentiments[i][1], "negative articles")
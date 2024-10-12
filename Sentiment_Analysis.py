from fastapi import FastAPI
from transformers import pipeline
from Main_Scraper import scrapeInfo

# used to figure out what stocks info we are on
counter = 0

pipe = pipeline("text-classification", model="mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")

app = FastAPI()

data, title, links = scrapeInfo(True, True)

# loops through every stock we asked for
for stock in data:
    print("\n\n\nNEW STOCK\n\n\n")
    # loops through every stocks individual news articles
    for i in range(len(stock)):
        # print(title[i])
        # print(links[i])
        # print(data[i])

        # get transformer result for data
        outputs = pipe(stock[i], top_k=None) # top_k=None just makes it so I get all the percentage results, not just the highest

        if outputs[0]['label'] == 'neutral':
            print('Low Confidence Title Was:', title[counter][i])
            print('Neutral or:', outputs[1]['label'])
        else:
            print('High Confidence Title Was:', title[counter][i])
            print(outputs[0]['label'])

    counter += 1
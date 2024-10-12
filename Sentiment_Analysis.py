from fastapi import FastAPI
from transformers import pipeline
from Main_Scraper import scrapeInfo

pipe = pipeline("text-classification", model="mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")

app = FastAPI()

data, title, links = scrapeInfo()

for i in range(len(data)):
    # print(title[i])
    # print(links[i])
    # print(data[i])
    outputs = pipe(data[i], top_k=None)
    if outputs[0]['label'] == 'neutral':
        print('Title was:', title[i])
        print('Neutral or:', outputs[1]['label'])
    else:
        print(outputs[0]['label'])
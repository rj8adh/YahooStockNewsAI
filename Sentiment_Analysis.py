from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from Main_Scraper import scrapeInfo
from openai import OpenAI

pipe = pipeline("text-classification", model="mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")

app = FastAPI()

data, title, links = scrapeInfo()

for i in range(len(data)):
    # print(title[i])
    # print(links[i])
    # print(data[i])
    outputs = pipe(data[i])
    print(outputs[0]['label'])
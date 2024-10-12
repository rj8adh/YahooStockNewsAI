from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from Main_Scraper import scrapeInfo
from openai import OpenAI

sentiment_pipe = pipeline("sentiment-analysis")

app = FastAPI()

data, title, links = scrapeInfo()

for i in range(len(data)):
    print(title[i])
    print(links[i])
    print(data[i])
    print(sentiment_pipe(data[i]))
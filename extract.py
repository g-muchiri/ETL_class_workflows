import pandas as pd
import requests
import json

def extract_articles():
    url = 'https://newsapi.org/v2/everything?q=apple&from=2026-07-31&to=2026-07-31&sortBy=popularity&apiKey=757a2dcfd035405b9fc631d9925f4d09'
    r = requests.get(url=url)
    test_data = r.json()
    articles_data = test_data['articles']
    articles_df = pd.DataFrame(articles_data)
    return articles_df
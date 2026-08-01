## In this Script, we will be refactoring our code
import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def extract_articles():
    url = f'https://newsapi.org/v2/everything?q=apple&from=2026-07-31&to=2026-07-31&sortBy=popularity&apiKey={os.getenv('NEWSAPIKEY')}'
    r = requests.get(url=url)
    test_data = r.json()
    articles_data = test_data['articles']
    articles_df = pd.DataFrame(articles_data)
    ##print('Part1 done')
    return articles_df


def transform_articles(articles_df):
    final_articles =articles_df.drop(columns=['source'])
    return final_articles


def load_articles(final_articles):
    from sqlalchemy import create_engine, text
    DATABASE_NAME = os.getenv('DATABASE_NAME')
    DATABASE_USER = os.getenv('DATABASE_USER')
    DATABASE_HOST = os.getenv('DATABASE_HOST')
    DATABASE_PORT = os.getenv('DATABASE_PORT')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

    engine = create_engine(f'postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}')
    with engine.connect() as conn:
        result = conn.execute(text('SELECT 1'))
        for i in result:
            print(i)

    final_articles.to_sql('articles', engine, if_exists='replace', index=False)


def main():
    data1 = extract_articles()
    data2 = transform_articles(data1)
    load_articles(data2)

    print("ETL Process Finished successfully")

if __name__ == "__main__":
    main()
    


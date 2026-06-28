import pandas as pd
import requests
import os
from dotenv import load_dotenv
load_dotenv()

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
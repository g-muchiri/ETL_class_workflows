import pandas as pd
def transform_articles(articles_df):
    articles_df = pd.DataFrame(articles_df)
    final_articles =articles_df.drop(columns=['source'])
    return final_articles.to_dict(orient="records")
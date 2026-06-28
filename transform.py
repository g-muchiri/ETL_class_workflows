def transform_articles(articles_df):
    final_articles =articles_df.drop(columns=['source'])
    return final_articles
import pandas as pd
def transform_articles(articles_df):
    final_articles =articles_df.drop(columns=['source'])

    ##dataframes are not easily "transportable and understandable" in software development word
    ##It is therefore important to convert our data to a json format for the purpose of returning
    return final_articles.to_dict(orient="records")
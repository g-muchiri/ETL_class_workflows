from extract import extract_articles
from transform import transform_articles
from load import load_articles


def main():
    data1 = extract_articles()
    data2 = transform_articles(data1)
    load_articles(data2)
    print("ETL Process Finished Very well")


if __name__ == "__main__":
    main()
    
    
    
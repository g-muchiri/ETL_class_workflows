# News API ETL_workflows
This is a basic beginner level project that takes us through the process of extracting, transforming and loading data from newsapi. The project is divided into three modules Extract, transform and load. The separation of these functions makes it easy to debug and tell where a problem rises from in the event it arises.

## Extract 🏭
Here we use libraries such as requests, json and pandas to read data from the API, convert json data into dictionary and finally to a dataframe that can be easily manipulated in the transform stage

## Transform 🧹
This project is not necessarily big on transform as we explore a few of the many pandas methods to transform. Here we explore dropping unnecessary columns as method of manipulation

## Load 🏬
We are loading the extracted and transformed data into a postgres database. Here we explore the use of libraries such as os and dotenv to enable us to read sensitive data from env.

In this module we explore use of `sqlalchemy` and `psycopg2` to create an engine that connects our code to the database.


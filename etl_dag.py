##This dag was ran in an folder with an environment containing airflow 

from datetime import timedelta, datetime
from airflow import DAG
##from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
   'articles_trial_3',
    description='Articles ETL',
    start_date=datetime(2026,7,1),
    schedule= timedelta(minutes=5),   #"@daily",
    catchup=False,
) as dag:

    task_c = BashOperator(
        task_id = 'Indicate_end',
        bash_command="""source ~/etl/etl_venv/bin/activate python3 ~/etl/pipeline.py"""
    )

    task_c
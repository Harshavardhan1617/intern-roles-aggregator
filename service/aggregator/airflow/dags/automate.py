from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

with DAG(dag_id="internships", start_date=datetime(2024, 12, 5), schedule="*/30 * * * *") as dag:
    hello = BashOperator(task_id="hello", bash_command="echo hello")


    @task()
    def airflow():
        print("airflow")

    hello >> airflow()
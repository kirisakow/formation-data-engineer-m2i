import datetime
from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator

@dag(dag_id="declaration_annotation",
    start_date = datetime.datetime(2023, 1, 1),
    schedule="@daily")
def generate_dag():
    EmptyOperator(task_id="task")

generate_dag()
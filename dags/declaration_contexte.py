import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="declaration_contexte",
    start_date = datetime.datetime(2023, 1, 1),
    schedule="@daily",
    default_args={"key":"value"}
):
    EmptyOperator(task_id="task")
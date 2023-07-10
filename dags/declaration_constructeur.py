import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

my_dag = DAG(
    dag_id="declaration_constructeur",
    start_date = datetime.datetime(2023, 1, 1),
    schedule="@daily",
    default_args={"key":"value"}
)

EmptyOperator(task_id="task", dag=my_dag)
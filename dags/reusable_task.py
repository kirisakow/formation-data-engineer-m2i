from airflow.decorators import dag, task
from datetime import datetime


@task
def sum(a, b):
    sum = a + b
    print(f'{a} + {b} = {sum}')
    return sum

@dag(dag_id='reusable_tasks', start_date=datetime(2023, 7, 12))
def reusable_dag():
    sum_0 = sum.override(task_id='sum_0')(3, 5)
    for i in range(1, 10):
        sum_0 >> sum.override(task_id=f'sum_{i}')(sum_0, i)

reusable_dag()
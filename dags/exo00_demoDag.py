# import de mes librairies
from __future__ import annotations
from datetime import datetime, timedelta
from textwrap import dedent
from airflow import DAG
from airflow.decorators import dag
from airflow.decorators import task

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

# with DAG(
#     dag_i="exercice_00",
#     default_args={
#         "depends_on_past": False,
#         "retries": 1,
#         "retry_delay": timedelta(minutes=5),
#     },
#     schedule="@daily",
#     start_date=datetime(2023, 7, 1),
#     catchup=False,
# ) as dag:

# mon_dag = DAG(
#     dag_i="exercice_00",
#     default_args={
#         "depends_on_past": False,
#         "retries": 1,
#         "retry_delay": timedelta(minutes=5),
#     },
#     schedule="@daily",
#     start_date=datetime(2023, 7, 1),
#     catchup=False,
# )

def ma_tache_t4():
    for i in range(5):
        today = datetime.today()
        print(today)
        print( str(today + timedelta(days=7)))

@dag(dag_id="exercice_00",
    default_args={
        "depends_on_past": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    schedule="@daily",
    start_date=datetime(2023, 7, 1),
    catchup=False,
)
def mon_dag():
    # tache 1
    t1 = BashOperator(
        task_id="print_date",
        bash_command="date",
        # dag=mon_dag,
    )
    # tache 2
    t2 = BashOperator(
        task_id="sleep",
        depends_on_past=False,
        bash_command="sleep 5",
        retries=3,
    )
    # templated_command = dedent(
    #     """
    # {% for i in range(5) %}
    #     echo "{{ ds }}"
    #     echo "{{ macros.ds_add(ds, 7)}}"
    # {% endfor %}
    # """
    # )
    # t3 = BashOperator(
    #     task_id="templated",
    #     depends_on_past=False,
    #     bash_command=templated_command,
    # )
    templated_python = dedent(
        """
    {% for i in range(5) %}
        print( "{{ ds }}" )
        print( "{{ macros.ds_add(ds, 7)}}" )
    """
    )

    t3 = PythonOperator(
        task_id="t4",
        depends_on_past=False,
        python_callable=lambda: ma_tache_t4()
    )
    

    t1 >> [t2, t3]


mon_dag()
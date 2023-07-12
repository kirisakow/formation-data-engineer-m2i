# import de mes librairies
from airflow.decorators import dag
from datetime import datetime, timedelta
from random import randint
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

def nb_random():
    return randint(0, 10000)

def save_inFile(file, **context):
    with open(file, "a") as f:
        msg = """date : {}, nombre aléatoire : {}
        """.format(
            context['execution_date'],
            nb_random()
        )
        f.write(msg)

@dag(
    dag_id="exercice_01",
    default_args={
        "depends_on_past": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    schedule="@daily",
    start_date=datetime(2023, 7, 1),
    catchup=True,
)
def mon_dag():

    # tache 1
    create_file = BashOperator(
        task_id="create-file",
        bash_command="/opt/airflow/dags/file/mon_script.sh ",
    )

    # tache 2
    save_data = PythonOperator(
        task_id="save_data",
        depends_on_past=False,
        python_callable=save_inFile,
        provide_context=True,
        op_kwargs={
            'file': '/opt/airflow/dags/file/rand_number.txt',
        },
    )

    create_file >> save_data

# appel de mon dag
mon_dag()


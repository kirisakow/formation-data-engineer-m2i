from airflow import DAG
from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import BranchPythonOperator
from datetime import datetime
import random


@dag(dag_id='branch_demo',
     start_date=datetime(2023, 7, 12),
     catchup=False)
def dag_1():
    t0 = EmptyOperator(task_id='t0')
    t1 = EmptyOperator(task_id='t1')
    t2 = EmptyOperator(task_id='t2')
    t3 = EmptyOperator(task_id='t3')
    t4 = EmptyOperator(task_id='t4')
    t5 = EmptyOperator(task_id='t5')
    t6 = EmptyOperator(task_id='t6')

    t0 >> t1
    t1 << t2
    t1 >> [t3, t4]
    t3 >> t5
    t4 >> t6


dag_1()


with DAG(dag_id='optional_branch_demo',
         start_date=datetime(2023, 7, 12),
         schedule='@once',
         catchup=False,
         default_args={'start_date': datetime(2023, 7, 12),
                       'retries': 1, }) as dag2:
    def choose_best_model_algorithm() -> str:
        accuracy = random.randint(0, 100)
        print(f'Accuracy: {accuracy}')
        if accuracy > 70:
            return ['super_accuracy', 'normal_accuracy']
        elif accuracy > 50:
            return 'normal_accuracy'
        else:
            return 'low_accuracy'

    t1 = DummyOperator(task_id='create_model')
    decision_algorithm = BranchPythonOperator(task_id='choose_best',
                                              python_callable=choose_best_model_algorithm)
    do_if_super_accuracy = DummyOperator(task_id='super_accuracy')
    do_if_normal_accuracy = DummyOperator(task_id='normal_accuracy')
    do_if_low_accuracy = DummyOperator(task_id='low_accuracy')

    t1 >> decision_algorithm >> [do_if_super_accuracy,
                                 do_if_normal_accuracy,
                                 do_if_low_accuracy]

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor
from airflow.exceptions import AirflowSensorTimeout
from datetime import datetime


def _failure_callback(context):
    if isinstance(context['exception'], AirflowSensorTimeout):
        print('sensor timeout')
        print(context)


def _store():
    print('store')


def _process():
    print('process')


with DAG(dag_id='demo_sensor',
        schedule_interval='@daily',
        catchup=False,
        start_date=datetime(2023, 7, 12)):

    partners = ['Jean', 'Karen', 'Jacqueline']
    filepath_tmpl = '/opt/airflow/dags/file/partner_{0}.txt'
    new_sensor = lambda name: FileSensor(task_id=f'sensor_{name}',
                                        filepath=filepath_tmpl.format(name),
                                        poke_interval=60,
                                        timeout=121,
                                        mode='poke',
                                        on_failure_callback=_failure_callback,
                                        fs_conn_id='fs_conn')
    check_partners_list = [new_sensor(p) for p in partners]

    t2 = PythonOperator(task_id='process_data', python_callable=_process)
    t3 = PythonOperator(task_id='store_data', python_callable=_store)

    check_partners_list >> t2 >> t3

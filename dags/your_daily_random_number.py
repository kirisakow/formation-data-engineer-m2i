import datetime
from airflow.decorators import dag, task
import random
import os


@dag(dag_id='your_daily_random_number',
     start_date=datetime.datetime(2023, 7, 1),
     schedule='@daily')
def your_daily_random_number(path_to_temporary_file: str,
                             path_to_definitive_file: str):

    def generate_str_of_random_digits(how_long: int = 8):
        return ''.join(random.choices('0123456789', k=how_long))

    @task(task_id='generate_and_temporarily_save_random_number')
    def t1_gen_random(path_to_temporary_file: str):
        with open(path_to_temporary_file, 'w') as tmp_file:
            tmp_file.write(generate_str_of_random_digits())

    @task(task_id='definitely_save_random_number')
    def t2_save_random(path_to_temporary_file: str,
                       path_to_definitive_file: str):
        field1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        field2 = '0' * 8
        if os.path.isfile(path_to_temporary_file):
            with open(path_to_temporary_file, 'r') as tmp_file:
                field2 = tmp_file.readline()
        with open(path_to_definitive_file, mode='a') as def_file:
            def_file.write(f'{field1},{field2}\n')

    @task(task_id='remove_temporary_file')
    def t3_remove_tmp(path_to_temporary_file: str):
        if os.path.isfile(path_to_temporary_file):
            os.remove(path_to_temporary_file)

    t1_gen_random(path_to_temporary_file) \
        >> t2_save_random(path_to_temporary_file, path_to_definitive_file) \
            >> t3_remove_tmp(path_to_temporary_file)


your_daily_random_number(
    path_to_temporary_file='/opt/airflow/your_daily_random_number/temp_storage.txt',
    path_to_definitive_file='/opt/airflow/your_daily_random_number/definitive_storage.csv'
)

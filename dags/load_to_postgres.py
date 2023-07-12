from airflow.decorators import dag, task
from datetime import datetime, timedelta
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.bash import BashOperator
import requests
import pandas as pd
import psycopg2 as pg


@dag(dag_id='drivers_data_extract_load_to_postgres',
     start_date=datetime(2023, 7, 11),
     schedule='@once',
     dagrun_timeout=timedelta(minutes=10))
def load_to_postgres(source_url: str,
                     path_to_csv: str,
                     dbname: str,
                     username: str,
                     password: str,
                     host: str):
    t1 = PostgresOperator(
        task_id='create_drivers_table',
        postgres_conn_id='tuto_pg_conn',
        sql='sql/create_drivers_table.sql'
    )

    @task(task_id='get_data_and_save_locally')
    def t2(url: str, path_to_csv: str):
        response = requests.get(url)
        if response.status_code == 200:
            df = pd.DataFrame(response.json())
            df.to_csv(path_to_csv, index=False)

    @task(task_id='load_data_to_postgres')
    def t3(dbname: str, username: str, password: str, host: str, path_to_csv: str):
        connection_uri = f"dbname='{dbname}' user='{username}' password='{password}' host='{host}'"
        try:
            with pg.connect(connection_uri) as pg_db_conn:
                cur = pg_db_conn.cursor()
                with open(path_to_csv, 'r') as data_src:
                    # skip the first line
                    next(data_src)
                    # iterate over the remaining lines
                    for row in data_src:
                        columns = row.split(',')
                        cur.execute("""
                            INSERT INTO drivers_data
                            VALUES ('{}', '{}', '{}', '{}', '{}')
                            """.format(
                                columns[0],
                                columns[1],
                                columns[2],
                                columns[3],
                                columns[4]
                            )
                        )
                pg_db_conn.commit()
        except Exception as e1:
            print(e1)

    t4 = BashOperator(
        task_id="delete_csv_file",
        bash_command=f"rm {path_to_csv}"
    )

    t1 >> t2(source_url, path_to_csv) \
        >> t3(dbname, username, password, host, path_to_csv) \
        >> t4


load_to_postgres(
    source_url='https://data.cityofnewyork.us/resource/4tqt-y424.json',
    path_to_csv='/opt/airflow/dags/data/drivers_data.csv',
    dbname='airflow',
    username='airflow',
    password='airflow',
    host='postgres',
)

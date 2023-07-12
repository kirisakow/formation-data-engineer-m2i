if [[ ! -e /opt/airflow/dags/file/rand_number.txt ]]; then
    mkdir -p "$AIRFLOW_HOME/dags/file"
    touch "$AIRFLOW_HOME/dags/file/rand_number.txt"
fi

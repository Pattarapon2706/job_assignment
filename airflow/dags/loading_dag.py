from airflow import DAG
from airflow.operators.python import PythonOperator
import logging
import subprocess
import os

from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 12, 21),
    'email_on_failure': False,
    'email_on_retry': False
}


def run_script(script_path):
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(script_path))
    
    print(script_dir)

    # Change the current working directory to the script directory
    os.chdir(script_dir)

    # Run the script
    result = subprocess.run(["python", script_path], capture_output=True, text=True)

    # Print the script output
    print("Script output:")
    print(result.stdout)

    # Check the exit code
    if result.returncode != 0:
        raise Exception(f"Script execution failed with exit code {result.returncode}. Error: {result.stderr}")

    return f"Script execution completed for {script_path}"

with DAG(
    'data_loading_dag',
    schedule_interval='@daily',
    default_args=default_args
) as dag:

    generate_sample_data = PythonOperator(
        task_id='generate_sample_data',
        python_callable=run_script,
        op_kwargs={'script_path': '/opt/airflow/dags/sample_data.py'},
        provide_context=True
    )

    load_data_to_postgres = PythonOperator(
        task_id='load_data_to_postgres',
        python_callable=run_script,
        op_kwargs={'script_path': '/opt/airflow/dags/data_loading.py'},
        provide_context=True
    )

    generate_sample_data >> load_data_to_postgres  # Set task dependency

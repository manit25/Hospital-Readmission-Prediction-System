from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

def run_ingestion():
    os.system("python ingestion/load_data.py")

def run_processing():
    os.system("python processing/spark_processing.py")

def run_model():
    os.system("python model/train_model.py")

default_args = {
    'owner': 'manit',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'hospital_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
)

t1 = PythonOperator(task_id='ingestion', python_callable=run_ingestion, dag=dag)
t2 = PythonOperator(task_id='processing', python_callable=run_processing, dag=dag)
t3 = PythonOperator(task_id='model_training', python_callable=run_model, dag=dag)

t1 >> t2 >> t3
from src.generators import data_generator as dg
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta, datetime
from pathlib import Path
import tempfile

cache = Path( tempfile.gettempdir() )

with DAG("itis",
         schedule=timedelta(minutes=1), 
         start_date=datetime(2025,1,1)
        ) as dag:

    send_consultation = PythonOperator(
        task_id="consultation",
        python_callable=dg.DataGenerator("consultation", 5*1024*1024,75).write, op_args=[cache] )
    
    send_event = PythonOperator(
        task_id="event",
        python_callable=dg.DataGenerator("event", 50*1024*1024,3).write, op_args=[cache] )
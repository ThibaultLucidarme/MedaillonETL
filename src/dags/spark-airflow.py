from datetime import datetime

import airflow
from airflow import DAG
from time import sleep
# from airflow.operators.python import PythonOperator
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.bash import BashOperator

from airflow.sdk import DAG, task, task_group


with DAG(
    dag_id = "sparking_flow",
    start_date = datetime(2026, 1, 1),
    schedule = "*/5 * * * *",
    catchup=False
) as dag:

    start = PythonOperator(
        task_id="start",
        python_callable = lambda: print("Job started"),
    )

    delay_bash_task = BashOperator(task_id="delay_bash_task",
                                             bash_command="sleep 5s")
    wait = PythonOperator(
        task_id="wait",
        python_callable = lambda: sleep(10),
    )



    end = PythonOperator(
        task_id="end",
        python_callable = lambda: print("Job completed successfully"),
    )

    start >> wait >> delay_bash_task >> end


    @task
    def get_nums():
        return [1, 2, 3]

    @task
    def times_2(num):
        return num * 2

    @task
    def add_10(num):
        return num + 10

    _get_nums = get_nums()
    _times_2 = times_2.expand(num=_get_nums)
    add_10.expand(num=_times_2)


    @task_group
    def op(num):
        @task
        def add_1(num):
            return num + 1

        @task
        def mul_2(num):
            return num * 2

        return mul_2(add_1(num))

    op.expand(num=[1, 2, 3])
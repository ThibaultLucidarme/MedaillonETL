FROM apache/airflow:latest-python3.11

USER airflow

RUN pip install apache-airflow apache-airflow-providers-apache-spark
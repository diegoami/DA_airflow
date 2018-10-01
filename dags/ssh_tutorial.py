"""
Code that goes along with the Airflow tutorial located at:
https://github.com/apache/incubator-airflow/blob/master/airflow/example_dags/tutorial.py
"""
from airflow import DAG
from airflow.contrib.operators.ssh_operator import SSHOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2018, 10, 1),
    'retry_delay': timedelta(minutes=5)
}
ssh_dag = DAG('ssh_tutorial', default_args=default_args)

from airflow.contrib.hooks.ssh_hook import SSHHook


hook = SSHHook(ssh_conn_id='SSH_228')
t3 = SSHOperator(
    task_id='ssh_task_1',
    command='ls >> ls.txt',
    ssh_hook=hook,
    dag=ssh_dag)


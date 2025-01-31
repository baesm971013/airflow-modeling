from datetime import datetime, timedelta
from textwrap import dedent

from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.trigger_rule import TriggerRule

default_args = {
    'owner': 'baesm',
    'depends_on_past': False,
    'email': ['your-email@g.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=15),
}

dag_args = dict(
    dag_id = "Baesm_example",
    default_args = default_args,
    description = "브랜치 설명",
    schedule_interval = timedelta(hours=4),
    start_date = datetime(2025,1,31),
    tags = ["example-baems"],
)



def random_branch_path():
    from random import randint          
    return "cal_a_id" if randint(1,2)==1 else "cal_m_id"

def calc_add(x,y,**kwargs):
    result = x+y
    print("x+y = ", result)
    kwargs['task_instance'].xcom_push(key="calc_result", value=result)
    return "calc add"

def calc_mul(x,y, **kwargs):
    result = x*y
    print("x*y = ", result)
    kwargs['task_instance'].xcom_push(key="calc_result", value=result)
    return "calc mul"

def print_result(**kwargs):
    r = kwargs['task_instance'].xcom_pull(key="calc_result")
    print("message:", r)
    print("*"*100)
    print(kwargs)
    


def end_seq():
    print("end")
    print("==="*30)
    
with DAG(**dag_args) as dag:
    start = BashOperator(
        task_id = "start",
        bash_command = "echo 시작!!!!!!!!!!!"
    )
    
    branch = BranchPythonOperator(
        task_id = "branch",
        python_callable = random_branch_path,
    )
    
    calc_add = PythonOperator(
        task_id = "cal_a_id",
        python_callable = calc_add,
        op_kwargs = {"x":10, "y":4}
    )
    
    calc_mul = PythonOperator(
        task_id = "cal_m_id",
        python_callable = calc_mul,
        op_kwargs = {"x":10, "y":4}
    )
    msg = PythonOperator(
        task_id='msg',
        python_callable=print_result,
        trigger_rule=TriggerRule.NONE_FAILED
    )

    complete_py = PythonOperator(
        task_id='complete_py',
        python_callable=end_seq,
        trigger_rule=TriggerRule.NONE_FAILED
    )

    complete = BashOperator(
        task_id='complete_bash',
        depends_on_past=False,
        bash_command='echo "complete~!"',
        trigger_rule=TriggerRule.NONE_FAILED
    )
    
    start >> branch >> calc_add >> msg >> complete_py >> complete
    start >> branch >> calc_mul >> msg >> complete
    
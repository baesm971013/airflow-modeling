# from datetime import datetime, timedelta
# from textwrap import dedent

# from airflow import DAG

# # Operators; we need this to operate!
# from airflow.operators.bash import BashOperator
# from airflow.operators.dummy import DummyOperator
# from airflow.operators.python import BranchPythonOperator
# from airflow.utils.trigger_rule import TriggerRule

# default_args = {
#     'owner': 'baem',
#     'depends_on_past': False,
#     'email': ['your-email@g.com'],
#     'email_on_failure': False,
#     'email_on_retry': False,
#     'retries': 1,
#     'retry_delay': timedelta(minutes=15),
# }

# dag_args = dict(
#     dag_id = "sequence_dag_example",
#     default_args = default_args,
#     description = "브랜치 설명",
#     schedule_interval = timedelta(minutes=50),
#     start_date = datetime(2024,1,30),
#     tags = ["example-baems"],
# )

# def random_branch_path():
#     from random import randint
    
#     return "path1" if randint(1,2)==1 else "my_name_en"

# with DAG(**dag_args) as dag:
    
#     t1 = BashOperator(
#         task_id = "print_date",
#         bash_command = "date",
#     )
    
#     t2 = BranchPythonOperator(
#         task_id = "branch",
#         python_callable = random_branch_path,
#     )
    
#     t3 = BashOperator(
#         task_id = "my_name_ko",
#         bash_command = 'echo "안녕하세요"',
#     )
    
#     t4 = BashOperator(
#         task_id = "my_name_en",
#         bash_command = 'echo "hi".'
#     )
    
#     complete = BashOperator(
#         task_id = "complete",
#         depends_on_past = False,
#         bash_command = 'echo "complete!!!!!"',
#         trigger_rule = TriggerRule.NONE_FAILED,
#     )
    
#     dummy1 = DummyOperator(
#         task_id="path1"
#     )
    
#     t1 >> t2 >>dummy1 >> t3 >> complete
#     t1 >> t2 >> t4 >> complete



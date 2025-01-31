# from airflow.decorators import dag, task
# from datetime import datetime, timedelta

# # 기본 설정
# default_args = {
#     "owner": "airflow",
#     "retries": 1,
#     "retry_delay": timedelta(minutes=5),
# }

# # DAG 정의
# @dag(
#     dag_id="baesm_decorator",
#     default_args=default_args,
#     schedule=timedelta(minutes=5),  # 5분마다 실행
#     start_date=datetime(2025, 1, 30, 16),  # 시작 날짜
#     catchup=False,  # 과거 실행 방지
#     tags=["example", "decorator"],  # 태그 추가
# )
# def hello_world_dag():
    
#     @task()
#     def print_hello():
#         print("Hello, Airflow!")

#     print_hello()  # 태스크 실행

# # DAG 인스턴스화
# hello_world_dag()
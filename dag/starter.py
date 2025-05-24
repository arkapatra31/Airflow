from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

with DAG(
    dag_id="starter_dag",
    schedule_interval="@daily",
    start_date=days_ago(1),
    catchup=False,
) as dag:
    task_1 = BashOperator(
        task_id="task_1",
        bash_command="date",
    )
    task_2 = BashOperator(
        task_id="task_2",
        bash_command="date",
    )
    task_3 = BashOperator(
        task_id="task_3",
        bash_command="date",
    )
    task_1 >> task_2 >> task_3

# Test the dag
if __name__ == "__main__":
    dag.run()

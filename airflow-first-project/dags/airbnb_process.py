from datetime import datetime
from airflow.sdk import DAG
import pendulum
from airflow.providers.standard.operators.bash import BashOperator

DBT_PROJECT_DIR = "/Users/cloudysunday/Documents/Github/dbt-tutorial/jaffle_shop"
DBT_PROFILE_DIR = "/Users/cloudysunday/.dbt"

default_args = {
    'owner': 'airflow',
    'retries': 1,
}

with DAG(
    dag_id = 'dbt_local_pipeline',
    start_date=pendulum.datetime(2024, 6, 1, tz="UTC"),
    schedule="0 0 * * *",
    catchup=False,
) as dag:
    
    dbt_debug = BashOperator(
        task_id='dbt_debug',
        bash_command=f"pwd",
    )

    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command=f"cd {DBT_PROJECT_DIR}  && source .venv/bin/activate && dbt run --profiles-dir {DBT_PROFILE_DIR}",
    )

    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command=f"cd {DBT_PROJECT_DIR}  && source .venv/bin/activate && dbt test --profiles-dir {DBT_PROFILE_DIR}",
    )

    dbt_debug >> dbt_run >> dbt_test
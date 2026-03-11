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
    dag_id = 'credit_card_pipeline',
    start_date=pendulum.datetime(2024, 6, 1, tz="UTC"),
    schedule="0 0 * * *",
    catchup=False,
) as dag:
    
    data_refresh = BashOperator(
        task_id='data_refresh',
        bash_command=f"pwd",
    )

    demographics = BashOperator(
        task_id='demographics',
        bash_command=f"echo demographics",
    )

    competitors = BashOperator(
        task_id='competitors',
        bash_command=f"echo competitors",
    )

    journey = BashOperator(
        task_id='journey',
        bash_command=f"echo journey",
    )

    hotspot = BashOperator(
        task_id='hotspot',
        bash_command=f"echo hotspot",
    )

    load_data_gcs = BashOperator(
        task_id='load_data_gcs',
        bash_command=f"echo load_data_gcs",
    )

    load_data_postgres = BashOperator(
        task_id='load_data_postgres',
        bash_command=f"echo load_data_postgres",
    )

    data_refresh >> [demographics, competitors, journey, hotspot]

    [demographics, competitors, journey, hotspot] >> load_data_gcs

    load_data_gcs >> load_data_postgres
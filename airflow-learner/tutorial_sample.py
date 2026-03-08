import json
import pendulum
from airflow.sdk import dag, task

@dag(
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def tutorial_sample():
    @task()
    def extract():
        list = [1, 2, 3, 4, 5]
        return list
    
    @task(multiple_outputs=True)
    def transform(list: list):
        sum = 0
        for i in list:
            sum += i
            print(f"Current sum is: {sum}")
        return {"sum": sum}
    
    @task()
    def load(sum: int):
        print(f"Final sum is: {sum}")

    extract_list = extract()
    sum = transform(extract_list)
    load(sum["sum"])
tutorial_sample()

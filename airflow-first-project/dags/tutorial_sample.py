import json 
import pendulum
from airflow.sdk import task, dag
@dag(
    schedule=None,
    start_date=pendulum.datetime(2024, 6, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def tutorial_sample():
    @task()
    def extract():
        data_string = '{"1001": 301.27, "1002": 433.21, "1003": 555.555}'
        order_data_dict = json.loads(data_string)
        return order_data_dict
    
    @task(multiple_outputs=True)
    def transform(order_data_dict: dict):
        total_order_value = 0
        for value in order_data_dict.values():
            total_order_value += value
        return {"total_order_value": total_order_value}
    
    @task()
    def load(total_order_value: float):
        print(f"Total order value is: {total_order_value}") 
    
    order_data = extract()
    transformed_data = transform(order_data)
    load(transformed_data["total_order_value"])
tutorial_sample()
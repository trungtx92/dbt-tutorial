import load_csv as csv
import os
import logging
import time
from google.cloud import bigquery
KEY_PATH = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
def main():
    
    client = bigquery.Client.from_service_account_json(KEY_PATH)
    csv.load_csv_to_bigquery_hosts(client)
    csv.load_csv_to_bigquery_listings(client)
    csv.load_csv_to_bigquery_reviews(client)

if __name__ == "__main__":
    main()

from google.cloud import bigquery
import os
import logging
# KEY_PATH = "secret/fictional-lab-dev-695729ef61c1.json"

def load_csv_to_bigquery(uri, table_id, table_schema, client):
    job_config = bigquery.LoadJobConfig(
        schema=table_schema,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        skip_leading_rows=1,
        source_format=bigquery.SourceFormat.CSV,
    )
    load_job = client.load_table_from_uri(
        uri,
        table_id,
        job_config=job_config
    )
    load_job.result()  # Waits for the job to complete.
    destination_table = client.get_table(table_id)
    print("Loaded {} rows.".format(destination_table.num_rows))
    # End of file: gcs_bq.py

def load_csv_to_bigquery_hosts(client):
    raw_hosts_schema=[
            bigquery.SchemaField("ID", "INTEGER"),
            bigquery.SchemaField("NAME", "STRING"),
            bigquery.SchemaField("IS_SUPERHOST", "STRING"),
            bigquery.SchemaField("CREATED_AT", "DATETIME"),
            bigquery.SchemaField("UPDATED_AT", "DATETIME"),
        ]
    load_csv_to_bigquery("gs://airbnb-tutorial/raw_hosts.csv", "airbnb.raw_hosts", raw_hosts_schema, client)

def load_csv_to_bigquery_listings(client):
    raw_listings_schema=[
            bigquery.SchemaField("ID", "INTEGER"),
            bigquery.SchemaField("LISTING_URL", "STRING"),
            bigquery.SchemaField("NAME", "STRING"),
            bigquery.SchemaField("ROOM_TYPE", "STRING"),
            bigquery.SchemaField("MINIMUM_NIGHTS", "INTEGER"),
            bigquery.SchemaField("HOST_ID", "INTEGER"),
            bigquery.SchemaField("PRICE", "STRING"),
            bigquery.SchemaField("CREATED_AT", "DATETIME"),
            bigquery.SchemaField("UPDATED_AT", "DATETIME"),
        ]
    load_csv_to_bigquery("gs://airbnb-tutorial/raw_listings.csv", "airbnb.raw_listings", raw_listings_schema, client)

def load_csv_to_bigquery_reviews(client):
    raw_reviews_schema=[
            bigquery.SchemaField("LISTING_ID", "INTEGER"),
            bigquery.SchemaField("DATE", "DATETIME"),
            bigquery.SchemaField("REVIEWER_NAME", "STRING"),
            bigquery.SchemaField("COMMENTS", "STRING"),
            bigquery.SchemaField("SENTIMENT", "STRING"),
        ]
    load_csv_to_bigquery("gs://airbnb-tutorial/raw_reviews.csv", "airbnb.raw_reviews", raw_reviews_schema, client)

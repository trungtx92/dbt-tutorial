from google.cloud import bigquery as bq
from datetime import datetime as dt

def export_table_to_gcs(project_id, dataset_id, table_id, gcs_bucket_name, file_name, client):
    job_config = bq.ExtractJobConfig(
        destination_format="CSV",         # or "PARQUET", "NEWLINE_DELIMITED_JSON", "AVRO"
        compression="GZIP",                # "GZIP", "NONE", "SNAPPY", etc.
        print_header=True,
    )

    extract_job = client.extract_table(
        f"{project_id}.{dataset_id}.{table_id}",
        f"{gcs_bucket_name}/{file_name}.csv.gz",
        job_config=job_config,
        location="US",  # Update this to your dataset's location
    )
    extract_job.result()  # Wait for the job to complete
    print(f"Exported {table_id} to {gcs_bucket_name}/{file_name}.csv.gz")
    print(f"Job ID: {extract_job.job_id}")
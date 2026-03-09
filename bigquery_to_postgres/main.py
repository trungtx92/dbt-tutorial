import constant as cst
import os
from google.cloud import bigquery as bq
from google.cloud import storage as gcs
import bigquery_to_gcs as bq2gcs
import gcs_to_postgres as gcs2pg
from datetime import datetime as dt
import time

KEY_PATH = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
DATETIME = dt.now().strftime("%Y%m%d%H%M")

def get_file_name(table_id):
    return f"{table_id}_{DATETIME}"

def main():
    bq_client = bq.Client.from_service_account_json(KEY_PATH)
    gcs_client = gcs.Client.from_service_account_json(KEY_PATH)
    file_name = get_file_name(cst.TABLE_ID)
    print("Running main function")

    bq2gcs.export_table_to_gcs(
        cst.PROJECT_ID,
        cst.DATASET_ID,
        cst.TABLE_ID,
        cst.GCS_BUCKET,
        file_name,
        bq_client
    )
    time.sleep(30)  # Wait for the file to be available in GCS
    gcs2pg.gcs_to_postgres(
        cst.GCS_BUCKET,
        cst.TABLE_ID,
        file_name,
        gcs_client
    )

if __name__ == "__main__":
    main()
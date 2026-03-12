import constant as cst
import os
from google.cloud import storage as gcs
import gcs_to_postgres as gcs2pg
from datetime import datetime as dt
import time

KEY_PATH = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
DATETIME = dt.now().strftime("%Y%m%d%H%M")

def get_file_name(table_id):
    return f"{table_id}"

def main():
    gcs_client = gcs.Client.from_service_account_json(KEY_PATH)
    file_name = get_file_name(cst.TABLE_ID)
    print("Running main function")
    # time.sleep(60)  # Wait for the file to be available in GCS
    gcs2pg.gcs_to_postgres(
        cst.GCS_BUCKET_NAME,
        cst.PG_TABLE_ID,
        file_name,
        gcs_client
    )

if __name__ == "__main__":
    main()
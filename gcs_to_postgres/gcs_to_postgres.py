
import psycopg2
from io import StringIO
from io import BytesIO
import constant as cst
import time
import gzip
import io

from google.cloud.exceptions import NotFound

def gcs_to_postgres(gcs_bucket_name, table_id, file_name, client):
    bucket = client.bucket(gcs_bucket_name)
    blob = bucket.blob(f"{file_name}.csv.gz")
    print(f"Downloading {file_name}.csv.gz from GCS bucket {gcs_bucket_name} ...")
    csv_data = BytesIO()
    #blob.download_to_file(csv_data)
    download_with_retry(blob, csv_data)
    csv_data.seek(0)
    conn = psycopg2.connect(
        host=cst.PG_HOST,
        database=cst.PG_DB,
        user=cst.PG_USER,
        password=cst.PG_PASSWORD,
        port=cst.PG_PORT
    )
    cur = conn.cursor()
    gz = gzip.GzipFile(fileobj=csv_data, mode="rb")
    text_stream = io.TextIOWrapper(gz, encoding="utf-8")
    try:
        cur.copy_expert(
            f"""
            COPY {table_id} FROM STDIN
            WITH (FORMAT CSV, HEADER TRUE, DELIMITER ',', NULL '\\N')
            """,
            text_stream
        )
        conn.commit()
        print(f"Data from {file_name}.csv.gz has been loaded into {table_id} in PostgreSQL.")
    finally:
        text_stream.detach()
        gz.close()
        cur.close()
        conn.close()

def download_with_retry(blob, destination_file, max_attempts=5, initial_delay=2):
    delay = initial_delay
    for attempt in range(1, max_attempts+1):
        try:
            blob.download_to_file(destination_file)
            print(f"Successfully downloaded {blob.name} on attempt {attempt}.")
            return
        except NotFound as e:
            if attempt == max_attempts:
                raise Exception(f"Failed to download {blob.name} after {max_attempts} attempts: {e}")
            print(f"Attempt {attempt} failed: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
            delay *= 2  # Exponential backoff
        except Exception as e:
            raise
            
            
    
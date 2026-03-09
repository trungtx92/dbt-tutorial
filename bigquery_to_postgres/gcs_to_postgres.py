
import psycopg2
from io import StringIO
import constant as cst
def gcs_to_postgres(gcs_bucket_name, table_id, file_name, client):
    bucket = client.bucket(gcs_bucket_name)
    blob = bucket.blob(f"{file_name}.csv.gz")
    print(f"Downloading {file_name}.csv.gz from GCS bucket {gcs_bucket_name}...")
    csv_data = StringIO()
    max_attempts = 12
    blob.download_to_file(csv_data)
    csv_data.seek(0)
    conn = psycopg2.connect(
        host=cst.PG_HOST,
        database=cst.PG_DB,
        user=cst.PG_USER,
        password=cst.PG_PASSWORD,
        port=cst.PG_PORT
    )
    cur = conn.cursor()
    cur.copy_expert(
        f"""
        COPY {table_id} FROM STDIN
        WITH (FORMAT CSV, HEADER TRUE, DELIMITER ',', NULL '\\N')
        """,
        csv_data
        )
    conn.commit()
    cur.close()
    conn.close()
    print(f"Data from {file_name}.csv.gz has been loaded into {table_id} in PostgreSQL.")

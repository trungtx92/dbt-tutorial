import load_csv as csv

def main():
    
    csv.load_csv_to_bigquery_hosts()
    csv.load_csv_to_bigquery_listings()
    csv.load_csv_to_bigquery_reviews()

if __name__ == "__main__":
    main()
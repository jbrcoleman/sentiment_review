from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
table_id = "reviews.reviews"

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("stars", "INTEGER"),
        bigquery.SchemaField("text", "STRING"),
    ],
    allow_quoted_newlines= True,
    ignore_unknown_values=True,
    max_bad_records=10,
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)
uri = "gs://reviews_yelp/yelp_reviews.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))

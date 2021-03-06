from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

def load_to_bigquery(table_id,review,sentiment):
    """
    load json record into bigquery Yelp review table
    """
    review= unicode(review, "utf-8")
    sentiment= unicode(sentiment, "utf-8")
    rows_to_insert=[
    {u"Review": review, u"Sentiment": sentiment},
    ]
    
    errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))

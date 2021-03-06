from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

def load_to_bigquery(table_id,review,sentiment):
    """
    load json record into bigquery Yelp review table
    """
    review= str(review)
    sentiment= int(sentiment)
    rows_to_insert=[
    {"Review": review, "Sentiment": sentiment},
    ]
    
    errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))
        
if __name__=='__main__':
    load_to_bigquery("reviews.predictions","This place was amazing",1)

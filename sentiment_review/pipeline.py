'''
This script is used to ingest a json file
from the Yelp review data set, prepare and transform the
JSON file to CSV,upload the file to the bucket,
then load to bigquery table. This script is 
scheduled to run once a day after
the daily yelp json reviews file has been
uploaded.
'''

# Imports the Google Cloud client library
from google.cloud import storage
from google.cloud import bigquery

import os
import time
import pandas as pd
import argparse
import numpy as np
from string import punctuation
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
import re

# Instantiates a client
storage_client = storage.Client()
# Construct a BigQuery client object.
bigquery_client = bigquery.Client()
#find_date
DATE = time.strftime("%Y%m%d")

def ingest(**kwargs):
    '''
    Ingest file from bucket to local machine
    '''
    if kwargs:
        file_link=kwargs[0]
    else:
        file_link='gs://reviews_yelp/yelp_academic_dataset_review.json'
    folder='data/'
    # Create this folder locally if not exists
    if not os.path.exists(folder):
        os.makedirs(folder)
    # Download the yelp review data
    with open(f'data/yelp_review-{DATE}.json','wb') as file_obj:
        storage_client.download_blob_to_file(
                file_link, file_obj)

def text_clean(review):
    '''
    clean up text
    '''
    # remove hypertext links
    review = re.sub(r'https?:\/\/.*[\r\n]*', '', review)
    # extract hash tag
    review = re.sub(r'@', '', review)
    # extract @
    review = re.sub(r'#', '', review)
    # extract numbers
    review = re.sub('[0-9]*[+-:]*[0-9]+', '', review)
    # extract '
    review = re.sub("'s", "", review)
    return review.strip().lower()

def remove_punc(string):
    return ''.join(x for x in string if x not in punctuation)

def remove_stopwords(string, stop_words):
    tokenized = word_tokenize(string)
    filtered_sentence = [word for word in tokenized if not word in stop_words]
    return ' '.join(c for c in filtered_sentence)

def transform_json_to_csv():
    '''
    Pull ingested json file from data directory
    and transform file to CSV
    '''
    review_json_path='../data/yelp_review.json'

    #Chunk data to help with memory issues
    size = 1000000
    review = pd.read_json(review_json_path, lines=True,
                          dtype={'review_id':str,'user_id':str,
                                 'business_id':str,'stars':int,
                                 'date':str,'text':str,'useful':int,
                                 'funny':int,'cool':int},
                          chunksize=size)
    chunk_list = []
    for chunk_review in review:
        #Drop unneeded columns
        chunk_review = chunk_review.drop(['review_id','user_id','business_id','date','useful','funny','cool'], axis=1)
        chunk_list.append(chunk_review)

    #Create Dataframe
    reviewdf=pd.concat(chunk_list, ignore_index=True, join='outer', axis=0)
    reviewdf['labels']  = np.where(reviewdf['stars']>3,1,0)
    reviewdf['text']=reviewdf['text'].apply(lambda x: text_clean(x))
    reviewdf['text']=reviewdf['text'].apply(lambda x: remove_punc(x))
    stop_words = set(stopwords.words('english'))
    reviewdf['text']=reviewdf['text'].apply(lambda x: remove_stopwords(x,stop_words))
    
    #Convert to CSV
    yelp_csv =f"../data/yelp_reviews-{DATE}.csv"
    reviewdf.to_csv(yelp_csv, index=False)
    

def upload():
    '''
    upload CSV file to bucket
    '''
    # Creating bucket object
    bucket = storage_client.get_bucket('reviews_yelp')
    # Name of the object to be stored in the bucket
    object_name_in_gcs_bucket = bucket.blob(f'yelp_reviews-{DATE}.csv')
    # Name of the object in local file system
    object_name_in_gcs_bucket.upload_from_filename(f'../data/yelp_reviews-{DATE}.csv')
    return object_name_in_gcs_bucket
def load_to_bigquery():
    '''
    load CSV file into bigquery Yelp review table
    '''
    #Set table_id to the ID of the table to create.
    table_id = "reviews.reviews"

    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("stars", "INTEGER"),
            bigquery.SchemaField("text", "STRING"),
            bigquery.SchemaField("labels", "INTEGER"),
        ],
        allow_quoted_newlines= True,
        ignore_unknown_values=True,
        max_bad_records=10,
        # The source format defaults to CSV, so the line below is optional.
        source_format=bigquery.SourceFormat.CSV,
    )
    uri = f"gs://reviews_yelp/yelp_reviews-{DATE}.csv"

    load_job = bigquery_client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )  # Make an API request.

    load_job.result()  # Waits for the job to complete.

    destination_table = bigquery_client.get_table(table_id)  # Make an API request.
    print("Loaded {} rows.".format(destination_table.num_rows))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Pass a yelp review json file to be uploaded to big query')
    parser.add_argument('-f','--file', action="store", default=None)
    args = parser.parse_args()
    
    if args.file is None:
        ingest()
        transform_json_to_csv()
        upload()
        load_to_bigquery()
    else:
        ingest(args.file)
        transform_json_to_csv()
        upload()
        load_to_bigquery()


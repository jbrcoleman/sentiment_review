# Imports the Google Cloud client library
from google.cloud import storage
import os

# Instantiates a client
storage_client = storage.Client()

folder='data/'
# Create this folder locally if not exists
if not os.path.exists(folder):
    os.makedirs(folder)
# Download the yelp review data
with open('data/yelp_review.json','wb') as file_obj:
    storage_client.download_blob_to_file(
        'gs://reviews_yelp/yelp_academic_dataset_review.json', file_obj)

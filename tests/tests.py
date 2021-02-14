from sentiment_review.main import multiply
import sentiment_review.pipeline
from google.cloud.storage import Blob
from google.cloud.storage import Client
from google.cloud.storage import Bucket
import time
import mock


def test_multiply():
    assert multiply(2,3)==6

#@mock_storage
#def test_ingest():
#    client = storage.Client()
#    # First, need to create a bucket in our virtual Google Cloud project
#    client.create_bucket("reviews_yelp")
#    bucket=bucket.get_bucket("reviews_yelp")
#    blob=Blob("yelp_academic_dataset_review.json",bucket)
#    with open("yelp_academic_dataset_review.json","rb") as my_file:
#        blob.upload_from_filename('yelp_academic_dataset_review.json')    
#    ingest('yelp_academic_dataset_review.json')
#    assert os.path.isfile('yelp_academic_dataset_review.json')

def test_upload():
    #find_date
    DATE = time.strftime("%Y%m%d")
    file_name=sentiment_review.pipeline.upload()

    assert file_name == f"yelp_reviews-{DATE}.csv" 

#def test_upload():
#        storage_client = mock.create_autospec(Client)
#        mock_bucket = mock.create_autospec(Bucket)
#        mock_blob = mock.create_autospec(Blob)
#        mock_bucket.return_value = mock_blob
#        storage_client.get_bucket.return_value = mock_bucket
#        mock_bucket.get_blob.return_value = mock_blob
#        mock_blob.download_as_string.return_value = "yelp_reviews-{DATE}.csv"
#        read_content = sentiment_review.pipeline.upload()
#        assert read_content == 'yelp_reviews-{DATE}.csv'


from sentiment_review.main import multiply
from sentiment_review.pipeline import remove_stopwords
from sentiment_review.pipeline import remove_punc
from sentiment_review.pipeline import text_clean
from nltk.corpus import stopwords
nltk.download()
# import sentiment_review.pipeline
# from google.cloud.storage import Blob
# from google.cloud.storage import Client
# from google.cloud.storage import Bucket
# import time
# import mock


def test_multiply():
    assert multiply(2, 3) == 6

def test_remove_stopwords():
    stop_words = set(stopwords.words("english"))
    test= "the dog jumped over the fence"
    ret="dog jumped fence"
    assert remove_stopwords(test,stop_words)==ret
    
def test_remove_punc():
    test= "Hi, how is you're cousin doing?"
    assert remove_punc(test)=="Hi how is youre cousin doing"
    
def test_text_clean():
    test= "https://google.com is one of the best website's I h@ve ever been to in since the 90's #google"
    ls=[]
    for word in test.split(' '):
        word=text_clean(word)
        ls.append(word)
    ls=' '.join(ls)
    assert ls==' is one of the best website i hve ever been to in since the  google'


# @mock_storage
# def test_ingest():
#    client = storage.Client()
#    # First, need to create a bucket in our virtual Google Cloud project
#    client.create_bucket("reviews_yelp")
#    bucket=bucket.get_bucket("reviews_yelp")
#    blob=Blob("yelp_academic_dataset_review.json",bucket)
#    with open("yelp_academic_dataset_review.json","rb") as my_file:
#        blob.upload_from_filename('yelp_academic_dataset_review.json')
#    ingest('yelp_academic_dataset_review.json')
#    assert os.path.isfile('yelp_academic_dataset_review.json')

# def test_upload():
# find_date
#    DATE = time.strftime("%Y%m%d")
#    file_name=sentiment_review.pipeline.upload()

#    assert file_name == f"yelp_reviews-{DATE}.csv"

# def test_upload():
#        storage_client = mock.create_autospec(Client)
#        mock_bucket = mock.create_autospec(Bucket)
#        mock_blob = mock.create_autospec(Blob)
#        mock_bucket.return_value = mock_blob
#        storage_client.get_bucket.return_value = mock_bucket
#        mock_bucket.get_blob.return_value = mock_blob
#        mock_blob.download_as_string.return_value = "yelp_reviews-{DATE}.csv"
#        read_content = sentiment_review.pipeline.upload()
#        assert read_content == 'yelp_reviews-{DATE}.csv'

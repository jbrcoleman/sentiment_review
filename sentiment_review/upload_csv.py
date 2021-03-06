from google.cloud import storage

# instantiate client
client = storage.Client()
# Creating bucket object
bucket = client.get_bucket("reviews_yelp")
# Name of the object to be stored in the bucket
object_name_in_gcs_bucket = bucket.blob("yelp_reviews.csv")
# Name of the object in local file system
object_name_in_gcs_bucket.upload_from_filename("../data/yelp_reviews.csv")

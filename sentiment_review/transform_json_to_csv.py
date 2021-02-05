import pandas as pd

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
reviewdf=pd.DataFrame(chunk_list)

#Convert to CSV
yelp_csv = "../data/yelp_reviews.csv"
reviewdf.to_csv(yelp_csv, index=False)


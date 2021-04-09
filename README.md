# Sentiment Analysis Project

This project used sentiment analysis on reviews posted to a python web app. The goal of this project was to create an automated process to connect with customers by sending them emails based on their emails. Customers who post negative reviews are sent emails with 50% off coupons to make up for their negative experince with the Coleman Company.

**Web APP link:** [Sentiment Analysis](dynamic-aurora-302220.uc.r.appspot.com)

## Sentiment Anaylsis

For this project I used Google's natural language automl service to build a sentiment analysis model. For the training data I used a dataset from Yelp that contained 8 million reviews. Before training the project the data was cleaned then stored into BigQuery for retrieval and analysis. The sentiment analysis model was built and deployed using Google Cloud's automl. Reviews written to the website are automatically sent to the deployed sentiment analysis model and results are stored in BiqQuery and sent to customer. An email is also sent to the customer. Customers who post negative reviews are sent emails with 50% off coupons to make up for their negative experince with the Coleman Company.  If you have trouble viewing email, please check your spam for message.  

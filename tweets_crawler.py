import tweepy
import pymongo
from pymongo import MongoClient
import requests

bearer_token = ''
# create clients
t_client = tweepy.Client(bearer_token, return_type=requests.Response)
m_client = MongoClient('localhost', 27017)
db = m_client['twitter_db']

# set queries and fields to retrieve
query = ['Elon','Musk','TWTR']
fields = ['text','author_id','id','created_at']

# Set end date to search tweets up to
# must be within 7 days before today
end_date = '2022-04-14T00:00:00Z'

# search for each query term
for word in query:
    # create collection for each different term
    term = 'twitter_' + word
    collection = db[term]
    # ensure each tweet is unique in collection
    collection.create_index([("id", pymongo.ASCENDING)], unique = True) 

    # search twitter api for term
    response = t_client.search_recent_tweets(word, max_results=60, tweet_fields=fields,end_time=end_date)

    # get json of response
    tweets_dict = response.json()
    tweets_data = tweets_dict['data']

    # insert each tweet into MongoDB
    index = 1
    for tweet in tweets_data:
        # print(str(index), end="")
        # print(tweet)
        # print("")
        print('tweet collected')
        try:
            collection.insert_one(tweet)
            index += 1
        except:
            pass
    


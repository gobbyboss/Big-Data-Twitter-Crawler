import tweepy
from pymongo import MongoClient
import requests


bearer_token = ""

# create clients
t_client = tweepy.Client(bearer_token, return_type=requests.Response)
m_client = MongoClient('localhost', 27017)
db = m_client['twitter_db']

query = ['sports']

# search for each query term
for word in query:
    # create collection for each different term
    term = 'twitter_' + word
    collection = db[term]

    # search twitter api for term
    response = t_client.search_recent_tweets(word, max_results=100)

    # get json of response
    tweets_dict = response.json()
    tweets_data = tweets_dict['data']

    # insert each tweet into MongoDB
    index = 1
    for tweet in tweets_data:
        print(str(index), end="")
        print(tweet)
        index += 1
        # collection.insert_one(tweet)
    


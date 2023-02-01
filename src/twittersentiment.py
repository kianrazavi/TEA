import tweepy
from tweepy import OAuthHandler
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def averages(tweets, type):
    total = 0
    for tweet in tweets:
        total += tweet['sentiment'][type]
    final_sentiment = total / len(tweets)
    return final_sentiment

class TwitterClient(object):
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console ==> do NOT push to repo
        consumer_key = 'XXX'
        consumer_secret = 'XXX'
        access_token = 'XXX'
        access_token_secret = 'XXX'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

        
    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using Vader's sentiment method
        '''
        # sentiment analyzer objects
        analyzer = SentimentIntensityAnalyzer()
        scores = []
        compound = []
        positives = []
        neutrals = []

        scores = analyzer.polarity_scores(tweet)

        compound = scores['compound']
        positives = scores['pos']
        neutrals = scores['neu']
        negatives = scores['neg']

        return {"Compound": compound, "Positive": positives, "Negative": negatives, "Neutral": neutrals}
    
    def get_tweets(self, query, count = 100):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search_tweets(q = query, count = count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets
        
        except tweepy.TweepyException as e:
            # print error (if any)
            print("Error : " + str(e))

    def return_sentiment(self, ticker):
            
        # initialize client
        api = TwitterClient()
            
        # accumulate tweets from ticker and company_name
        tweets = api.get_tweets(query = ticker, count = 1000)
        #print(tweets)
        #tweets.extend(api.get_tweets(query = company_name, count = 500)) ==> eventually when we can do names as well
        try:
            # get avg sentiments for each type
            comp = averages(tweets, 'Compound')
            pos = averages(tweets, 'Positive')
            neu = averages(tweets, 'Neutral')
            neg = averages(tweets, 'Negative')
            return {"Compound": comp, "Positive": pos, "Negative": neg, "Neutral": neu}
        except:
             print("Error: No tweets with such ticker found")
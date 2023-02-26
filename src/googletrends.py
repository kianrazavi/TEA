import pytrends as pt
import pandas as pd 
import numpy as np
from pytrends.request import TrendReq
import os 


class Trends():
    def __init__(self, keywords):

        # should be in a string list format, all the key words 
        self.keywords = keywords

        # set to 1 month by default 
        self.timeframe = 'today 3-m'

        # set the geography, by default we set it to New York in the US to get wallstreet saturated data

        self.geo = 'US-NY'
        #set the category of the search data 
        self.cat =  1179


        self.df = pd.DataFrame()

    def raw_trends(self):

        # get the raw trend data from the pytrends library 

        pytrends = TrendReq(hl='en-US', tz=360)

        kw_list = self.keywords

        # build the API Call
        pytrends.build_payload(kw_list, cat=self.cat, timeframe=self.timeframe, geo=self.geo)

        daily_trends = pytrends.interest_over_time()

        return daily_trends


    def publish_data(self, name):
        # publish the trends data to a csv in some path
        daily_trends = self.raw_trends()

        daily_trends.to_csv(os.path.join('/Users/martinturuta/Desktop/Pandas Tutorial/Trends output', name))



test = Trends(['TESLA'])
test.publish_data('test.csv')
import yfinance as yf 
import datetime as dt
import numpy as np
import pandas as pd

### here we'll pull all pricing information and make any functions for technical calculations.
# For RSI, for example: https://www.qmr.ai/relative-strength-index-rsi-in-python/

class Prices(): 
    def __init__(self, ticker):
        self.ticker = ticker

    def get_prices(self):

        # define time interval to pull from 
        start_date = (dt.date.today() - dt.timedelta(days=30)).strftime("%Y-%m-%d")
        end_date = dt.date.today().strftime("%Y-%m-%d")


        # perform yahoo functions 
        symbol = yf.Ticker(self.ticker)
        df = symbol.history(interval="1d", start=start_date, end=end_date)
        return df 
    
    def get_rsi(self):
        # gets the rsi value on a daily time grain
        pass

    def get_momentum(self):
        # gets the momentum factor on a daily time grain 
        pass


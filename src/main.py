from twittersentiment import TwitterClient

def main():

    api = TwitterClient()

    # user enters ticker (and eventually company name)
    inp = input("Enter stock ticker: ")
    # if ticker, look up company name and vice versa
    # gather twitter info
    ticker = '$' + inp.upper()
    twitter_sentiment_score = api.return_sentiment(ticker)
    
    print(twitter_sentiment_score)


if __name__ == "__main__":
    # calling main function
	main()
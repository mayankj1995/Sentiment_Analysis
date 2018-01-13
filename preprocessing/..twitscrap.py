from twitterscraper import query_tweets


# All tweets matching either Trump or Clinton will be returned. You will get at
# least 10 results within the minimal possible time/number of requests
#for tweet in query_tweets("Google")[:5]:
#	print(tweet.user)
for tweet in query_tweets("#facebook since:2017-12-04 until:2017-12-05", 10)[:10]:
    print(tweet.text.encode('utf-8'))
    print(tweet.timestamp)

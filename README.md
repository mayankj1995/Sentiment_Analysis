# Sentiment_Analysis
Analyzing news and twitter sentiment using Naive Bayes Classifier to predict stock prices

First Install some of these programs that you will need.
Use the following code for that
	sudo pip install -U textblob
	sudo pip install twitterscraper
	sudo pip install tweet-preprocessor
	sudo pip install pyenchant
	
Hypothesis - Is News sentiment more accurate compared to Twitter Sentiment in predicting stock market.

In this project we use Naive Bayes Classifier to train and test our dataset of news and tweets

There are three folders in this project
- preprocessing - This contains all the code to collect and clean the dataset, so that we can use it easily to train and classify

- tmp - This contains all the datasets that we collect

- training - This contains the code that we use to train our datasets and analyze it

# preprocessing folder

There are 6 files in this folder.

a) get_articles.py - This program uses the News API to collect news, and saves the news to tmp/news_data/Raw_News

b) clean_news_data.py - This program takes the dataset from Raw_News and cleans it by getting rid of unknown characters, and concantenating the news with the same date. It saves the new datset in tmp/news_data/Clean_News
						
c) get_stock_data.py - We already have the Stock price data save in the tmp/stock_data folder. This program takes the stock data, Calculates the price change, normalizes it and returns a dataframe.
						
d) get_tweets.py - This program uses the library 'twitterscrapper' to fetch tweets that go back to many years. This program get tweets for a particular stock for the last two years. It then clean the dataset by getting rid of unknown characters
						
e) clean_tweet_data.py - This program removes all the punctuations, non-english words, extra-spaces, and returns a nice clean dataset. It saves the news dataset in tmp/tweet_data/Clean_Data
						
f) combining_data.py - This program combines the news, twitter and stock price data into a singel dataset and saves it in the tmp/training_data/ folder.
						
The training_data folder has two files for each stock. We use the 2015-2016 year as the training dataset. and the 2016-2017 as the test datsaet.
	
# training folder
There are two files in this folder.

a) train_twitter_data.py - This program takes in the training data from the tmp/training_data folder and trains the Naive Bayes classifier. Then it prints out the accuracy of the classifier by testing it with the test dataset. It also saves the results in the tmp/results/twitter folder. 

b) train_news_data.py - It does the same thing as the above train_twitter_data.py, but with the news data.

import pandas as pd
import numpy as np

from get_stock_data import get_stock_data
#from clean_news_data import get_news_data 


def combine_all_data(ticker):
    #Import all data
   
    #stock_path = '../tmp/stock_data/' + ticker + '2015-2016.csv'
    print "Combining All data"
    news_path =  '../tmp/news_data/Clean_News/' +  ticker + '_clean_data.csv'
    tweet_path = '../tmp/tweet_data/Clean_Tweets/' +  ticker + '_clean_data.csv'
    
    stock_df = get_stock_data(ticker)
    news_df = pd.read_csv(news_path)
    tweet_df = pd.read_csv(tweet_path)
    
    print tweet_df.head(n=5)
    price_change = []
    tweets = []
    
    #Join data by date
    for index, row in news_df.iterrows():
        val = stock_df.loc[stock_df['Date'] == row[0],'Change'].values
        price_change.append('pos' if (val > 0.0) else 'neg' )
        tweets.append(tweet_df.loc[tweet_df['Date'] == row[0],'Tweets'].values)
    
    #Add new column to news dataset
    news_df['price change'] = price_change
    news_df['tweets'] = tweets
    #Add new column to news dataset
    #news_df['tweets'] = tweets
    news_df['tweets']= news_df['tweets'].str[0]
    
    #Drop rows with null price change cells
    news_df.dropna(subset=['price change'], inplace=True)
    news_df.dropna(subset=['tweets'], inplace=True)
    news_df = news_df.reset_index(drop=True)

    #print final dataset
    print "\nThe final dataset\n"
    print news_df[['date','snippet','tweets','price change']].head(n=10)
    
    path = '../tmp/training_data/' +  ticker + '_data1.csv'
    news_df.to_csv(path, encoding = 'utf-8',index=False) 
    return news_df
combine_all_data('AMZN2015-2016')
combine_all_data('AMZN2016-2017')


'''''
combine_all_data('AAPL2015-2016')
combine_all_data('AAPL2016-2017')

combine_all_data('FB2015-2016')
combine_all_data('FB2016-2017')

combine_all_data('TSLA2015-2016')
combine_all_data('TSLA2016-2017')

combine_all_data('MSFT2015-2016')
combine_all_data('MSFT2016-2017')
'''
 
 
 
 

import pandas as pd
import numpy as np
from textblob.classifiers import NaiveBayesClassifier



#from textblob import TextBlob
def train__twitter_data(ticker):
   
    
    df = pd.read_csv('../tmp/training_data/' + ticker + '2015-2016_data1.csv')
    train_df = df[['tweets','price change']]
    print "Training Tweets Dataset"
    print train_df.head(5)
    cl = NaiveBayesClassifier(train_df.as_matrix(columns=None))
    #with open('../tmp/tweet_data/FB_data2.csv', 'r') as fp:
    #    cl = NaiveBayesClassifier(fp, format="csv")
    
    
    df = pd.read_csv('../tmp/training_data/' + ticker + '2016-2017_data1.csv')
    dataset = df[['tweets','price change']]
    
    classified = []
    right = 0
    #print dataset.head(n=5)
    print "\nClassifying dataset\n"
    for index, row in dataset.iterrows():
        classified.append(cl.classify(row[0]))
        right += 1 if row[1] == classified[index] else 0
        
    dataset['Tweet Sent.'] = classified
    path = '../tmp/results/Tweets/' + ticker + '_results.csv'
    dataset.to_csv(path, encoding = 'utf-8',index=False)
    #dataset['Price Sent.'] = real_sent
    print dataset[['tweets','price change','Tweet Sent.']].head(n=20)
    total = len(dataset['tweets'])
    print "\nCalculating "
    print "\nCorrect %d, Total %d" %(right, total)
    print "Correct percentage %.2f %%" %((1.0*right/total)*100)
    #print cl.classify(dataset.as_matrix(columns=None))
    print cl.show_informative_features(10)
    #print cl.accuracy(dataset.as_matrix(columns=None))
train__twitter_data('AMZN')
'''''
train__twitter_data('AAPL')
train__twitter_data('FB')
train__twitter_data('MSFT')

train__twitter_data('TSLA')
'''

    #print cl.show_informative_features(100)
    #print "Classifing this sentence: \n With growing competition from the likes of " + \
    #    "Google and Amazon, Apple appears to be working to improve its relationship with app makers."
    #print cl.classify("With growing competition from the likes of Google and Amazon, Apple appears to be working to improve its relationship with app makers.")
    
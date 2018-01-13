import pandas as pd
import numpy as np
from textblob.classifiers import NaiveBayesClassifier



from textblob import TextBlob
def train_data(ticker):
   
    
    df = pd.read_csv('../tmp/training_data/' + ticker + '2015-2016_data1.csv')
    train_df = df[['snippet','price change']]
    print "Training News Dataset"
    print train_df.head(5)
    cl = NaiveBayesClassifier(train_df.as_matrix(columns=None))
    
    df = pd.read_csv('../tmp/training_data/' + ticker + '2016-2017_data1.csv')
    dataset = df[['snippet','price change']]
    
    classified = []
    right = 0
    #print dataset.head(n=5)
    print "\nClassifying dataset\n"
    for index, row in dataset.iterrows():
        classified.append(cl.classify(row[0]))
        right += 1 if row[1] == classified[index] else 0
       
    dataset['News Sent.'] = classified
    path = '../tmp/results/News/' + ticker + '_results.csv'
    dataset.to_csv(path, encoding = 'utf-8',index=False)
    #dataset['Price Sent.'] = real_sent
    print dataset[['snippet','price change','News Sent.']].head(n=20)
    total = len(dataset['snippet'])
    print "\nCalculating "
    print "\nRight %d, Total %d" %(right, total)
    print "Correct percentage %.2f %%" %((1.0*right/total)*100)
    #print cl.classify(dataset.as_matrix(columns=None))
    print cl.show_informative_features(10)
    #print cl.accuracy(dataset[['snippet','price change']].as_matrix(columns=None))
train_data('AMZN')
'''''
train_data('AAPL')
train_data('FB')
train_data('MSFT')
train_data('TSLA')
'''

    #print cl.show_informative_features(100)
    #print "Classifing this sentence: \n With growing competition from the likes of " + \
    #    "Google and Amazon, Apple appears to be working to improve its relationship with app makers."
    #print cl.classify("With growing competition from the likes of Google and Amazon, Apple appears to be working to improve its relationship with app makers.")
    

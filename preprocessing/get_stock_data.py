import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

def get_stock_data(ticker):
    
    print 'Getting Stock Prices\n'
    #Importing the csv file downloaded from yahoo finance
    path = '../tmp/stock_data/' + ticker + '.csv'
    stock_df = pd.read_csv(path)
    stock_df = stock_df[['Date','Open','Close']]
        
    #Normalizing data    
    stock_df['Change'] = ((stock_df['Close'] - stock_df['Open'])/(stock_df['Open']))
    maxm = max(abs(stock_df['Change']))
    stock_df['Change'] = stock_df['Change'] / (maxm)
    
    #Getting rid of Open and Close prices
    stock_df = stock_df[['Date','Change']]
  
    #Print first 5 rows of the data
    #print stock_df.head(n=5)
    
    return stock_df
    

#get_stock_data('FB')

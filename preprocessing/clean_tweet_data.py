import pandas as pd
import numpy as np
import re
import enchant

def get_tweet_data(ticker):
    print 'Getting Stock Tweets\n'
    path = '../tmp/tweet_data/Raw_Tweets/' + ticker + '.csv'
    df = pd.read_csv(path,encoding="ISO-8859-1")
    
    #Drop empty values
    df.dropna(subset=['Tweets'], inplace=True)
    df = df.reset_index(drop=True)
    
    printable = set(['\x0c', ' ', 'D', 'H', 'L', 'P', 'T', 'X', 'd','h', 'l', 'p', 't', 'x', '\x0b', 'C', 'G', 'K', 'O', 'S', 'W',  'c', 'g', 'k', 'o', 's', 'w', '\n','B', 'F', 'J', 'N', 'R', 'V', 'Z', 'b', 'f', 'j', 'n', 'r', 'v', 'z', '\t', '\r', 'A', 'E', 'I', 'M', 'Q', 'U', 'Y', 'a', 'e', 'i', 'm', 'q', 'u', 'y'])
    new_arr = []
    size = 0
    d = enchant.Dict("en_US")
    
    for index, row in df.iterrows():
        new_arr.append([])
        new_arr[size].append(row[0])
        
        text = re.sub(' +',' ',str(filter(lambda x: x in printable,row[1]))).lower()
        english_words = []
        for word in text.split():
            if d.check(word):
                english_words.append(word)
            #else:
                #print word
        text = " ".join(english_words)

        new_arr[size].append(text)
        size +=1
    clean_df = pd.DataFrame(new_arr)
    clean_df.columns = ['Date', 'Tweets']
    print df.head(n=20)
    #Sort by Date
    clean_df = clean_df.sort_values(by=['Date'])
    clean_df = clean_df.reset_index(drop=True)
    
    
    print clean_df.head(n=20)
    #print df.head(n=20)
    path = '../tmp/tweet_data/Clean_Tweets/' +  ticker + '_clean_data.csv'
    clean_df.to_csv(path, encoding = 'utf-8',index=False)
    return df
    
get_tweet_data('AMZN2015-2016')
get_tweet_data('AMZN2016-2017')
'''''
get_tweet_data('AAPL2015-2016')
get_tweet_data('AAPL2016-2017')

get_tweet_data('FB2015-2016')
get_tweet_data('FB2016-2017')

get_tweet_data('TSLA2015-2016')
get_tweet_data('TSLA2016-2017')

get_tweet_data('MSFT2015-2016')
get_tweet_data('MSFT2016-2017')
'''




   
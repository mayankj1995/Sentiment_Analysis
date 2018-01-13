import pandas as pd
import numpy as np


def get_news_data(ticker):
    print 'Cleaning Stock News\n'
    path = '../tmp/news_data/Raw_News/' + ticker + '.csv'
    df = pd.read_csv(path,encoding="ISO-8859-1")
    
    #Dropping the unnecessary columns
    df = df[['pub_date','snippet']]
    
    #Trimming the Date column and renaming it
    df['pub_date'] = df['pub_date'].astype(str).str[0:10]
    df.rename(columns={'pub_date': 'date'}, inplace = True)
    
    #Drop empty values
    df.dropna(subset=['snippet'], inplace=True)
    df = df.reset_index(drop=True)
    
    printable = set(['\x0c',',', ' ', 'D', 'H', 'L', 'P', 'T', 'X', 'd','h', 'l', 'p', 't', 'x', '\x0b', 'C', 'G', 'K', 'O', 'S', 'W',  'c', 'g', 'k', 'o', 's', 'w', '\n','B', 'F', 'J', 'N', 'R', 'V', 'Z', 'b', 'f', 'j', 'n', 'r', 'v', 'z', '\t', '\r', 'A', 'E', 'I', 'M', 'Q', 'U', 'Y', 'a', 'e', 'i', 'm', 'q', 'u', 'y'])
    new_arr = []
    size = 0
    for index, row in df.iterrows():
        new_arr.append([])
        new_arr[size].append(row[0])
        new_arr[size].append(str(filter(lambda x: x in printable,row[1])))
        size +=1
    clean_df = pd.DataFrame(new_arr)
    clean_df.columns = ['date', 'snippet']
    print df.head(n=20)
    #Sort by Date
    clean_df = clean_df.sort_values(by=['date'])
    clean_df = clean_df.reset_index(drop=True)
    
    
    #Combining news with same date
    clean_df = clean_df.groupby(df['date'])['snippet'].apply(' '.join)
    clean_df = clean_df.reset_index()
    print clean_df.head(n=20)
    #print df.head(n=20)
    path = '../tmp/news_data/Clean_News/' +  ticker + '_clean_data.csv'
    clean_df.to_csv(path, encoding = 'utf-8',index=False)
    return df
    
get_news_data('AMZN2015-2016')
get_news_data('AMZN2016-2017')
''''
get_news_data('AAPL2015-2016')
get_news_data('AAPL2016-2017')    

get_news_data('FB2015-2016')
get_news_data('FB2016-2017')

get_news_data('TSLA2015-2016')
get_news_data('TSLA2016-2017')

get_news_data('MSFT2015-2016')
get_news_data('MSFT2016-2017')
'''





   
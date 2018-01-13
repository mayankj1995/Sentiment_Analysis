from twitterscraper import query_tweets
import preprocessor as p
import datetime
import string
import pandas as pd




# at least 10 results within the minimal possible time/number of requests

def get_tweets(query, date_from,date_until ):
    tweets = ""
    #characters we want in the tweets
    printable = set(['\x0c','.',',','!',' ', 'D', 'H', 'L', 'P', 'T', 'X', 'd','h', 'l', 'p', 't', 'x', '\x0b', 'C', 'G', 'K', 'O', 'S', 'W',  'c', 'g', 'k', 'o', 's', 'w', '\n','B', 'F', 'J', 'N', 'R', 'V', 'Z', 'b', 'f', 'j', 'n', 'r', 'v', 'z', '\t', '\r', 'A', 'E', 'I', 'M', 'Q', 'U', 'Y', 'a', 'e', 'i', 'm', 'q', 'u', 'y'])
    #Combining 20 tweets for each day
    for tweet in query_tweets(query + " since:" + date_from + " until:" + date_until, 20)[:20]:
        tweets = tweets + " " + str(filter(lambda x: x in printable,p.clean(tweet.text.encode('utf-8'))))
    return tweets
        

def get_all_tweets(query,date_from,date_until):
    #Converting into datetime format to add days to date
    print "Getting Tweets data for %s" %(query)
    start_date = datetime.datetime.strptime(date_from, '%Y-%m-%d')
    print "From: " + start_date.strftime('%Y-%m-%d')
    end_date = start_date + datetime.timedelta(days=1)
    final_date = datetime.datetime.strptime(date_until, '%Y-%m-%d')
    print "Until: " + final_date.strftime('%Y-%m-%d')
    print "This might take a while"
    #Creating matrix to later add to the dataframe
    matrix = []
    size=0
    while end_date <= final_date:
        #Apending an array in the matrix for Date, Tweet
        matrix.append([])
        
        #Appending date,Tweet to the array
        matrix[size].append(start_date.strftime('%Y-%m-%d')) #Converting to the required date format
        matrix[size].append(get_tweets(query,start_date.strftime('%Y-%m-%d') , end_date.strftime('%Y-%m-%d') ))
        #Increment the size
        size +=1
        print "Getting tweets from %s" %(start_date.strftime('%Y-%m-%d'))
        
        #Adding 1 day to the start_date and the end_date
        start_date = start_date + datetime.timedelta(days=1)
        end_date = start_date + datetime.timedelta(days=1)
    #Creating a dateframe of that matrix    
    df = pd.DataFrame(matrix)
    #Changing column names of the dataframe
    df.columns = ['Date', 'Tweets']
    return df
def dump_data(query,ticker):
    data = get_all_tweets(query,'2015-12-01','2015-12-11')
    path = '../tmp/tweet_data/Raw_Tweets/test' +  ticker + '2015-2016.csv'
    data.to_csv(path, encoding = 'utf-8',index=False)
    data = get_all_tweets(query,'2016-12-01','2016-12-11')
    path = '../tmp/tweet_data/Raw_Tweets/test' +  ticker + '2016-2017.csv'
    data.to_csv(path, encoding = 'utf-8',index=False)
    print ticker + ' done' 
       
def main():
    dump_data('#AMZN OR #amazon', 'AMZN')
    #dump_data('#facebook','FB')
    #dump_data('#AAPL OR #apple', 'AAPL')
    #dump_data('#TSLA OR #tesla','TSLA')
    #dump_data('#MSFT OR #microsoft', 'MSFT')
    
    
    

main()
#print matrix

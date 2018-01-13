import requests
from math import ceil
from time import sleep
import csv
import pandas as pd
from itertools import chain

def get_nyt_articles(api_key, query, begin_date, end_date, page):
    """
    Make a basic call to the NYT articles API
    `begin_date` and `end_date` are in YYYYMMDD format
    returns a dict object
    """
    articles_endpoint = "http://api.nytimes.com/svc/search/v2/articlesearch.json"
    the_params = {
        "api-key"    : api_key,
        "q"           : query,
        #"fq"         : 'source.contains:("New York Times")',
        "begin_date" : begin_date,
        "end_date"   : end_date,
        "page": page
    }
    response = requests.get(articles_endpoint, params = the_params)
    if response:
        return response.json()
    else:
        return 0


def get_all_articles(query,api_key,begin_date,end_date):
    print "Getting all articles for " + query + "from " + begin_date + " to " + end_date + ". This might take some time"
    all_articles = []
    articles = articles_endpoint = "http://api.nytimes.com/svc/search/v2/articlesearch.json"
    for i in range(0,10): #NYT limits pager to first 100 pages. But rarely will you find over 100 pages of results anyway.
        response = get_nyt_articles(api_key,query, begin_date,end_date, str(i))
        sleep(0.5)
        if response!=0:
            response = response['response']
            docs = response['docs']
            all_articles.append(docs)

            print(str(i))
            sleep(0.5)
    return(all_articles)


def main():
    search_term = 'amazon'
    ticker = 'AMZN'
    #Get all articles and save it into the array
    all_articles2 = get_all_articles(search_term,"ba4ff4ab3e754274a6c7a831d0379dd7", '20151201', '20161201')

    #Create a dataframe from the array
    #Clean the Data using clean_news_data function
    data = pd.DataFrame(list(chain.from_iterable(all_articles2)))

    #Save the data as a csv file
    path = '../tmp/news_data/Raw_News/test' +  ticker + '2015-2016.csv'
    clean_data.to_csv(path, encoding = 'utf-8',index=False)

main()

# keys = all_articles2[0].keys()
# with open('all_articles_apple.csv', 'w') as output_file:
#     dict_writer = csv.DictWriter(output_file, keys)
#     dict_writer.writeheader()
#     dict_writer.writerows(all_articles2)



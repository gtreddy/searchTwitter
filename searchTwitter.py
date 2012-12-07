import urllib2
import json
import sys
def search_twitter(query='python'):
  url = 'http://search.twitter.com/search.json?q=' + query
  response = urllib2.urlopen(url).read()
  data = json.loads(response)
  return data['results']

def print_tweets(tweets):
  for tweet in tweets:
    print tweet['from_user'] + ': ' + tweet['text'] + '\n'

if __name__ == "__main__":
  query=raw_input("Input what you want to search: ")
 
  results = search_twitter(query)
  print_tweets(results)
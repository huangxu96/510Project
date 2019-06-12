from __future__ import absolute_import, print_function
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import csv


consumer_key='8l38rrT5sRZA2Xu2OnpKjVEjb'
consumer_secret='ZVHO4kE5Lg655peFC5ysEMf8WyEfouWJTvZtVDfC2HuliOWglN'



access_token='2390456413-Z0zYToRU7ceV06TJ40pyrpKzVX5CKb41DgLI9h1'
access_token_secret='yrLwPl9gweAcH35Dn93aS2tHYuXG3jowGnvmk7SlFghWH'

class StdOutListener(StreamListener):
    """ 
    A listener handles tweets that are received from the stream.     
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        with open('measles.csv', 'a') as f:
            f.write(data)
        print(data)

        return True
    def on_error(self, status):
        print(status)
if __name__ == '__main__':

    text = open('text.txt', 'w')
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['measles'], languages=['en'])
    text.close()


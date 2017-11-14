# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 19:54:50 2017

@author: Zina Wang
"""

from __future__ import absolute_import, print_function
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="lf2os47YyaqwzNRJwmHnGhnFn"
consumer_secret="dffJg0HZ3DVYXVhgrdNFtPxEJor8UHOtPfZLseWQL2WywliHLb"
# After the step above, you will be redirected to your app’s page.
# Create an access token under the the "Your access token" section
access_token="930476805735243777-woNLralvo7nj0b2KUZdiKi6gv7J9XUp"
access_token_secret="BFwgQWV9smOKFhuiR5sDnxHBlrWHDiTfilFp4BUTEZaZz"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        # print data
        parsed_json = json.loads(data)
        
        # print parsed_json['place']['bounding_box']['coordinates']
        
        print (json.dumps(parsed_json,indent=4))
        fi = open("C:/Users/Zina Wang/git/ams.json",'a')
        fi.write(data)
        fi.close()
        
        return True
    def on_error(self, status):
        print(status)
        
if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.sample()

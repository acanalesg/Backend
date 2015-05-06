from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import time

consumer_key = "zSUVYhsjhh7fcqF7VdDsH25GE";
consumer_secret = "Trg8dRkTpNH25u3yteWRhiLzarGaeeb3pDNKsQDy6YWkHQmy2B";
access_token = "2809827652-6pzODCcXwm26dgEyXrzcxa4pgdkUFSdFdWsNOOF";
access_token_secret = "LZdX6A9fUiKSn5Zqv8ELW8uBp8rlUTcqn1BvKkAZ8RkDN";

# file name that you want to open is the second argument
save_file = open('datos.json', 'a')



class listener(StreamListener):

    def on_data(self, data):
        print(data)
        #json_data = json.loads(data)
        save_file.write(str(data))
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["nepal"])


"""import the necassary methods from the tweepy library, StreamListener, OAuthHandler,
Stream"""


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


"""Variables for credentials to access 
Twitter API"""

from secret import access_token_secret, access_token, consumer_secret, consumer_key


"""listener to twitter that prints recieved tweets to standout (stdout)"""


class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    """HANDLES twitter authentication and connection to twitter 
    streaming API"""


l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)


"""code to filter the captured data by the keywords
"insert", "insert", "insert"""


stream.filter(track=['uber', 'lyft', 'taxi'])
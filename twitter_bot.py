# import the neccassry libraries
# install Tweepy using this command >   pip3 install tweepy

import tweepy
import time

# Twitter Keys
CONSUMER_KEY = '----'
CONSUMER_SECRET = '----'
ACCESS_KEY = '----'
ACCESS_SECRET = '----'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


# retrieve and store last seen ID's
FILE_NAME = 'lastSeenId.txt'


# retrieve last seen ID's
def retrieveLastSeenId(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


# store last seen ID's
def storeLastSeenID(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

    
# bot replying to tweets
def replying_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    last_seen_id = retrieveLastSeenId(FILE_NAME)

    # use tweet_mode='extended' to show full tweets details
    mentions = api.mentions_timeline(
        last_seen_id,
        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        storeLastSeenID(last_seen_id, FILE_NAME)
        if '#helloworld' in mention.full_text.lower():
            api.update_status('@' + mention.user.screen_name +
                              '#HelloWorld back to you!', mention.id)


while True:
    replying_to_tweets()
    time.sleep(12)

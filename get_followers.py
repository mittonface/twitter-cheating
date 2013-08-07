from secret_stuff import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET
import twitter


KEYWORD = "Matt Smith"
NUM_STATUSES = 150

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_SECRET)

tweets = api.GetSearch(KEYWORD, count=NUM_STATUSES)

for tweet in tweets:
    if not tweet.GetFavorited():
        try:
            api.CreateFavorite(tweet)
        except twitter.TwitterError:
            print "That's a failure!"


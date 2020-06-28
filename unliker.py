import tweepy

privatefile = open('nothankyou.txt', 'r')
consumer_key = privatefile.readLine()
consumer_secret = privatefile.readLine()
access_token = privatefile.readLine()
access_token_secret = privatefile.readLine()
privatefile.close()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
timeline = api.user_timeline("ArielBissett")

print(timeline)
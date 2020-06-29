# import os
import tweepy

privatefile = open('nothankyou.txt', 'r')
consumer_key = privatefile.readLine()
consumer_secret = privatefile.readLine()
# access_token = privatefile.readLine()
#access_token_secret = privatefile.readLine()
privatefile.close()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback='oob')
auth_url = auth.get_authorization_url()
print('Authorization URL: ' + auth_url)

verifier = input('PIN: ').strip()
auth.get_access_token(verifier)
print('ACCESS_KEY = "%s"' % auth.access_token)
print('ACCESS_SECRET = "%s"' % auth.access_token_secret)

auth.set_access_token(auth.access_token, auth.access_token_secret)

api = tweepy.API(auth)
timeline = api.user_timeline("ArielBissett")
username = api.me()
print(username)
print(timeline)
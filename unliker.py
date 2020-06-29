# thanks to https://gist.github.com/hezhao/4772180

# import os
import tweepy

privatefile = open('nothankyou.txt', 'r')
consumer_key = privatefile.readline().strip()
consumer_secret = privatefile.readline().strip()
test = privatefile.readline().strip()
# access_token = privatefile.readline()
#access_token_secret = privatefile.readline()
privatefile.close()

print(consumer_key, consumer_secret, test)

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
username = username["name"]
print(username)
print(timeline)
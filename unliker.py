# thanks to https://gist.github.com/hezhao/4772180
# thanks to https://stackoverflow.com/questions/49589497/how-to-get-an-users-liked-favourited-tweets-with-tweepy-python3

import tweepy

# Grabs your consumer key and secret key from a text file.
privatefile = open('nothankyou.txt', 'r')
consumer_key = privatefile.readline().strip()
consumer_secret = privatefile.readline().strip()
privatefile.close()

# Callback as oob allows us to use the PIN method instead of the callback method. 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback='oob')
auth_url = auth.get_authorization_url()
print('Authorization URL: ' + auth_url)
print('Return here and paste the PIN with ctrl-shift-v. Note that this will UNLIKE ALL OF YOUR TWEETS!')
verifier = input('PIN: ').strip()
auth.get_access_token(verifier)
print('ACCESS_KEY = "%s"' % auth.access_token)
print('ACCESS_SECRET = "%s"' % auth.access_token_secret)
auth.set_access_token(auth.access_token, auth.access_token_secret)

# wait_on_rate_limit ensures we don't violate Twitter's rate limits, locking us out. 
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

username = api.me()
username = username._json
id = username['id']
screenname = username['screenname']

# how long we're going to iterate
favorites_count = username['favourites_count']

print(screenname)
print(id)
print(favorites_count)

# for each like, delete it
# for favorite in tweepy.Cursor(api.favorites, id=id).items(favorites_count):
for favorite in tweepy.Cursor(api.favorites, id=id).items(2):
    # print('Tweet author: '+str(favorite.user.screen_name.encode("utf-8")))
    print('Tweet ID: '+str(favorite.id))
    print(favorite)
    # api.destroy_favorite(favorite.id)
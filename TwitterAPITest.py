# -*- coding:utf-8 -*-
from TwitterAPI import TwitterAPI, TwitterPager

SCREEN_NAME = 'tianhel1'
SEARCH_TERM = '#Trump'
TWEET_ID = '1311633424428404736'

consumer_key = ""
consumer_secret = ""

api = TwitterAPI(consumer_key,
                 consumer_secret,
                 auth_type='oAuth2')

#This shows all the information of a certain user
				 
r = api.request('users/lookup', {'screen_name':SCREEN_NAME})
print(r.json() if r.status_code == 200 else 'PROBLEM: ' + r.text)

#get tweet by ID

r = api.request('statuses/show/:' + TWEET_ID)
tweet = r.json()
print(tweet['user']['screen_name'] + ':' + tweet['text'] if r.status_code == 200 
      else 'PROBLEM: ' + r.text)

#Search 10 tweets about Trump

r = api.request('search/tweets', {'q': SEARCH_TERM,'count':10})

for item in r:
    print(item['text'].encode('gbk', 'backslashreplace').decode('gbk', 'backslashreplace') if 'text' in item else item)

print('\nQUOTA: %s' % r.get_quota())
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, json, urllib, random, bitly_api

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

dpla_data = "http://api.dp.la/v2/items?q=canada+OR+canadian+OR+tim+horton+OR+timbits+OR+maple+OR+poutine+OR+hockey+OR+curling+OR+molson+OR+labatt+OR+quebecois+OR+ontario+OR+quebec+OR+alberta+OR+british+columbia+OR+saskatchewan+OR+yukon+OR+samsquanch+OR+manitoba+OR+nova+scotia+OR+new+brunswick+OR+pei+OR+newfoundland&page_size=500&api_key=91b1bb54a822c576aa55d1b7a9babbd6"

response = urllib.urlopen(dpla_data);
data = json.loads(response.read())
docs = data["docs"]

items = random.sample(docs,1)

for item in items:
  url = item["isShownAt"]
  description = item["sourceResource"]["title"]
  eh = "#eh?"
  description = description + "\n" + eh
  if len(description) > 103:
    while len(description) + 3 > 102:
      description = description[:len(description) - 1]
    description = description + '...'
  tweet_text = "%s %s" % (description,url)
  api.update_status(tweet_text)

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

dpla_data = "http://api.dp.la/v2/items?sourceResource.description=canada+OR+canadian+OR+%22tim+horton%22+OR+timbits+OR+maple+OR+poutine+OR+hockey+OR+curling+OR+molson+OR+labatt+OR+quebecois+OR+ontario+OR+quebec+OR+alberta+OR+%22british+columbia%22+OR+saskatchewan+OR+yukon+OR+samsquanch+OR+manitoba+OR+%22nova+scotia%22+OR+%22new+brunswick%22+OR+pei+OR+%22prince+edward+island%22+OR+newfoundland+OR+labrador+OR+%22northwest+territories%22+OR+nunavut+OR+moose+OR+loon*+OR+sorry+OR+toronto+OR+snow+OR+igloo+OR+toque+OR+beaver+OR+beavertail+OR+lacross+OR+zamboni+OR+%22ice+skates%22+OR+puffinpage_size=500&api_key=91b1bb54a822c576aa55d1b7a9babbd6"

response = urllib.urlopen(dpla_data);
data = json.loads(response.read())
docs = data["docs"]

items = random.sample(docs,1)

for item in items:
  url = "https://dp.la/item/" + item["id"]
  description = item["sourceResource"]["description"][0]
  description = (description[:104] + '...') if len(description) > 104 else description
  if len(description) <= 1:
      break
  cancon = "#CanCon"
  canadian_flag = u'\U0001F1E8\U0001F1E6'
  maple_leaf = u'\U0001F341'
  description = description + "\n" + " " + maple_leaf + " " + canadian_flag + " " + cancon
  tweet_text = "%s %s" % (description,url)
  api.update_status(tweet_text)

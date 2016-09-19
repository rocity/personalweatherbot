import json
import secrets
from TwitterAPI import TwitterAPI
from weather import getWeather

lastid = ""

# get last tweet id to whom we replied to
with open('idstr.json', 'r') as openfile:
    savedid = json.load(openfile)
    lastid = savedid['laststr']

# initialize twitter api
t = TwitterAPI(secrets.APIKEY,
               secrets.APISECRET,
               secrets.ACCESSTOKEN,
               secrets.ACCESSTOKENSECRET)

# secrets.watch: Screen name to observe tweets on
r = t.request('statuses/mentions_timeline', {
    'screen_name': secrets.WATCH,
    'since_id': lastid,
    'count': 1
    })

for tweet in r:
    print("latest tweet: %s" % tweet['id_str'])
    print("last replied to: %s" % lastid)
    if tweet['id_str'] != lastid:
        
        print("replying to %s" % tweet['id_str'])
        reply_text = getWeather(tweet['user']['screen_name'])
        print(reply_text)

        # with open('idstr.json', 'w') as outfile:
            # save last tweet to json file
            # json.dump({'laststr': tweet['id_str']}, outfile)
    else:
        print('no new tweets')

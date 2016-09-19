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

def bot():
    # secrets.watch: Screen name to observe tweets on
    r = t.request('statuses/mentions_timeline', {
        'screen_name': secrets.WATCH,
        'since_id': lastid,
        'count': 1
        })

    for tweet in r:
        # check if the latest tweet is the one we replied to last
        if tweet['id_str'] != lastid:
            # generate a reply to the tweet using the weather module
            reply_text = getWeather(tweet['user']['screen_name'])
            print(reply_text)

            # send a reply to the tweet
            newreply = t.request('statuses/update', {
                'status': reply_text,
                'in_reply_to_status_id': tweet['id_str']
                })

            # save last tweet to a json file
            with open('idstr.json', 'w') as outfile:
                json.dump({'laststr': tweet['id_str']}, outfile)
        else:
            print('no new tweets')

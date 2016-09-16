from urllib.request import urlopen
import json
import secrets
import twitter
import codecs

reader = codecs.getreader("utf-8")

# initialize twitter api
t = twitter.Api(consumer_key=secrets.APIKEY,
                  consumer_secret=secrets.APISECRET,
                  access_token_key=secrets.ACCESSTOKEN,
                  access_token_secret=secrets.ACCESSTOKENSECRET)

response = urlopen(secrets.WEATHERURL).read().decode('utf8')
parsed_json = json.loads(response)

location = parsed_json['current_observation']['display_location']['city']
tempc = parsed_json['current_observation']['temp_c']
weather = parsed_json['current_observation']['weather']
obstime = parsed_json['current_observation']['observation_time']

report_text = "Current temperature in %s is %sc at %s. %s" % (location, tempc, weather, obstime)
master_report = "%s %s" % (secrets.GREETING, report_text)

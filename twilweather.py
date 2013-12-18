# PIP INSTALL twilio
# PIP INSTALL weatherpy
# Twilio Docs - https://github.com/twilio/twilio-python
# Weatherpy Docs - https://github.com/cmcdowell/weatherpy

from twilio.rest import TwilioRestClient
import weatherpy

#ADD CREDENTIALS
account = "xxxxxxxxxx"
token = "xxxxxxxxxx"

#ADD YOUR TWILIO NUMBER
twilioNumber = "+xxxxxxxxxx"


# ADD RECIPIENT (IF USING TWILIO FREE ACCOUNT, THE NUMBER MUST BE VERIFIED) 
sendTo = "+xxxxxxxxxx"

# ADD LOCATION USING WOEID (2442047 is Los Angeles, CA)
# WOEID LOOKUP - http://woeid.rosselliot.co.nz/
woeid = 2442047


r = weatherpy.Response("Weatherpy Service", woeid, metric=False)
units = r.units
wind = r.wind
conditions = r.condition
forecasts = r.forecasts
astro = r.astronomy
location = r.location

# Returns WOEID location string eg. Current conditions for Los Angeles:
getLocation =  'Current conditions for {0}:'.format(
    location.city,
)

#Returns Temperature and conditions eg. 56 F, Weather: Fair 
getTemperature = '{0} {1}, Weather: {2}'.format(
    conditions.temperature,
    units.temperature,
    conditions.text
)
#Returns Wind Speed eg. 0.0 mph,
getWind = 'Wind: {0} {1} ,'.format(
    wind.speed,
    units.speed,
)
#Returns Time of Sunrise and Sunset
getSunrise =  astro.sunrise
getSunset = astro.sunset

 
client = TwilioRestClient(account, token)

# Sends Message, requires to, from_ & body
message = client.messages.create(to=sendTo, from_= twilioNumber,
                                body= "%s %s %s Sunrise: %s, Sunset: %s." % (getLocation, getTemperature, getWind, getSunrise, getSunset))

# Prints results
print "Success! Sending: " + message.body +" To: " + message.to + " From: " + message.from_

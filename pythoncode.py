import urllib2
import json
from sys import stdout
import time
import requests
import geocoder
import urllib



while True:
#polling for latitude and longitude positions of International Space Station
        req = urllib2.Request("http://api.open-notify.org/iss-now.json")#get request
        response = urllib2.urlopen(req)
	obj = json.loads(response.read())
        lat= obj['iss_position']['latitude']#store latitude position
        lon= obj['iss_position']['longitude']   # store longitude position
        g = geocoder.google([float(lat), float(lon)], method='reverse') #to locate country/international waters based on latitude and longitude
        if g.country_long == None: #if no country, then international waters
                loc="International Waters"
        else:
                loc=g.country_long #else print country name
        print(loc)      
	print obj['timestamp'] #print time when latitude and longitude are recorded
        print '{"latitude is":"%s","longitude is":"%s"}'%(lat, lon) #print latitude and longitude
        stdout.flush() #flush to stdout
        time.sleep(5) # 5 seconds because it has been stated in the website that polling every 5 seconds would give accurate results.

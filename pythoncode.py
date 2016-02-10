import urllib2
import json
from sys import stdout
import time

while True:
#polling for latitude and longitude positions of International Space Station
        req = urllib2.Request("http://api.open-notify.org/iss-now.json")#get request
        response = urllib2.urlopen(req)

        obj = json.loads(response.read())
        lat= obj['iss_position']['latitude']#store latitude position
        lon= obj['iss_position']['longitude']   # store longitude position
        print obj['timestamp'] #print time when latitude and longitude are recorded
        print '{"latitude is":"%s","longitude is":"%s"}'%(lat, lon)
        stdout.flush() #flush to stdout
        req2= urllib2.Request("http://maps.google.com/?q=lat,lon")
        time.sleep(5) # 5 seconds because it has been stated in the website that polling every 5 seconds would give accurate results.
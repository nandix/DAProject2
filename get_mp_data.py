#!/usr/bin/python

import urllib, json, csv


urlpre = "https://www.mountainproject.com/data?action=getRoutes&routeIds="
urlpost = "&key=111347304-d2112ad3994252fce499dd91a8f629d8"

n_queries = 5000
n_per_q = 200
step = 10

last_time = 0 # Number of queries we got to last time

routeIDi = 105748391 + last_time*n_per_q*step
# routeIDi =   105748000

f = csv.writer(open("dat1.csv", "wb+"))
# Write CSV Header, If you dont need that, remove this line
f.writerow(["rating", "stars", "pitches", "type", "city", "state"])

#{u'routes': [{u'rating': u'5.9 R', u'name': u'Gravel Pilot', u'url': u'https://www.mountainproject.com/v/gravel-pilot/105748400', u'imgMed': u'', u'pitches': u'1', u'starVotes': u'1', u'imgSmall': u'', u'location': [u'Colorado', u'Boulder', u'Boulder Canyon', u'Stepping Stones'], u'stars': u'3.0', u'type': u'Trad, TR', u'id': u'105748400'}], u'success': 1}

# loop over all routes we care about
for i in range(0, n_queries):
    print "Processing query ", i
    # construct a string of the next 100 route IDs
    urlmiddle = str(routeIDi)

    for ID in range(routeIDi+step, routeIDi+step*n_per_q, step):
        urlmiddle = urlmiddle + "," + str(ID)

    # Increment the route ID to start at
    routeIDi = routeIDi + n_per_q*step

    url = urlpre + urlmiddle + urlpost

    response = urllib.urlopen(url)
    data = json.loads(response.read())

    print data
    for x in data['routes']:

        try: 
            if len(x["location"]) >= 2:

                # print x
                # print x["name"]
                # print x["rating"]
                # print x["stars"]
                # print x["pitches"]
                # print x["type"]
                # print x["location"][1]
                # print x["location"][0]
                f.writerow([x["name"], x["rating"], x["stars"],x["pitches"], x["type"], x["location"][1], x["location"][0]])
        except:
            print "Couldn't handle case: ", routeIDi
            pass


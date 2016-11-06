#url = 'http://WebName?route=route1'

#Using a url passed as an argument write the current route and the next post
#to a text file and save it
def CreateRoute(routeName):
    #imports
##    import urlparse

##    #get route from the url
##    parsed = urlparse.urlparse(url)
##    route = urlparse.parse_qs(parsed.query)['route'][0]
    

    #dictionary containing all routes
    #route number mapped to list of postIds in the order to be visited
    allRoutes = { "route1" : ["visitorCentre", "kelpies" ], "route2" : ["stuff", "things"] }

    #get the chosen route
    route = allRoutes[routeName]

    #set the next post to the first post in the route
    nextPost = route[0]

    #write the route and next post to a .txt file
    f = open('currentRoute.txt', 'w')
    for post in route:
        f.write(post + ',')
    f.write('\n' + nextPost + '\n')
    f.close()

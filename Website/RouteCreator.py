#url = 'http://WebName?route=route1'

def CreateRoute(url):

    #imports
    import urlparse

    #get route from the url
    parsed = urlparse.urlparse(url)
    route = urlparse.parse_qs(parsed.query)['route'][0]

    #dictionary containing all routes
    #route number mapped to list of postIds in the order to be visited
    allRoutes = { "route1" : ["visitorCentre", "kelpies", "docks"], "route2" : ['stuff', 'things'] }

    #get the chosen route
    route = allRoutes[route]

    #build a dictionary to determine which posts
##    visited = {}
##    for post in currentRoute:
##        visited[post] = False
    nextPost = route[0]

    f = open('currentRoute.txt', 'w')

    for post in route:
        f.write(post + ',')
    f.write('\n' + nextPost + '\n')
    
    f.close()

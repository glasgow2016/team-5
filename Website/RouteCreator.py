import urlparse

url = 'http://WebName?route=route1'
parsed = urlparse.urlparse(url)
route = urlparse.parse_qs(parsed.query)['route'][0]

allRoutes = { "route1" : ["visitor centre", "kelpies", "docks"], "route2" : ['stuff', 'things'] }

currentRoute = allRoutes[route]

visited = {}
for post in currentRoute:
    visited[post] = False

print visited

f = open('currentRoute.txt', 'w')

for post in currentRoute:
    f.write(post + ',')
f.write('\n')

for post in currentRoute:
    f.write(str(visited[post]) + ',')
f.write('\n')

f.close()

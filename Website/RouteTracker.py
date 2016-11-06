#url = 'http://WebName?time=1478870000.00&postId=visitorCentre'

def UpdateRoute(url):

    #imports
    import urlparse
    import os
    import time

    #get the postId and time qr was generated from url
    parsed = urlparse.urlparse(url)
    postId = urlparse.parse_qs(parsed.query)['postId'][0]
    qrTime = float(urlparse.parse_qs(parsed.query)['time'][0])

    #compares the current time with time qr code was generated
    #if the qr code was generated less than 5 minutes ago then
    #it is valid and route can be updated
    if time.time() - qrTime < 300:

        f = open("currentRoute.txt", 'r')

        line = f.readline()[:-2]
        route = line.split(',')

        nextPost = f.readline()[:-1]

        f.close()

        if postId == nextPost:

            if postId == route[-1]:
                os.remove('currentRoute.txt')
                return True
                
            else:

                nextPost = [route.index(postId) + 1]
                
                f = open('currentRoute.txt', 'w')

                for post in route:
                    f.write(post + ',')
                f.write('\n')

                for post in route:
                    f.write(str(visited[post]) + ',')
                f.write('\n' + nextPost + '\n')

                f.close()
                return False

        else:
            return 'Wrong Post'
    else:
        return 'Invalid QR code'


#sample url = '52.211.235.179:5000/posts/kelpie?time=1478870000.00&postId=kelpie'

def UpdateRoute(qrTime, postId):

    #imports
##    import urlparse
    import os
    import time

##    #get the postId and time qr was generated from url
##    parsed = urlparse.urlparse(url)
##    qrTime = float(urlparse.parse_qs(parsed.query)['time'][0])
##    postId = urlparse.parse_qs(parsed.query)['postId'][0]    

    #compares the current time with time qr code was generated
    #if the qr code was generated less than 5 minutes ago then
    #it is valid and route can be updated
    if time.time() - qrTime < 300:

        f = open("currentRoute.txt", 'r')

        #read first line and get the routeas a list
        line = f.readline()[:-2]
        route = line.split(',')

        #get the next post to visit
        nextPost = f.readline()[:-1]

        f.close()

        #check if the post scanned is the next post on the route
        if postId == nextPost:

            #check if the post scanned is the last post on the route
            #if so then delete the current route file and return True
            if postId == route[-1]:
                os.remove('currentRoute.txt')
                return True

            #else then find the next post on the route and update the file
            #and return False
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
            
##        else:
##            return 'Wrong Post'
##    else:
##        return 'Invalid QR code'


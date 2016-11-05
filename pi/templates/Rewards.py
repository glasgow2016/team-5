import string
import random

def ValidateReward(stickerList,n):
    if len(stickerList)==n:
        chars=string.ascii_uppercase + string.digits
        print ''.join(random.choice(chars)for _ in range(6))
    
                      

ValidateReward(stickerList,n)

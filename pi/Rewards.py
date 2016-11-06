import string
import random

##Check if user has all stickers, then generate reward code
def ValidateReward(stickerList,n):
    if len(stickerList)==n:
        
        ##Generate Random Reward code
        chars=string.ascii_uppercase + string.digits
        print ''.join(random.choice(chars)for _ in range(6))
    
##ValidateReward(stickerList,n)

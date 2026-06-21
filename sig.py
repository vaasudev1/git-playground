#import the required components
import hmac
import hashlib
def signature(key,message):
    #create a new hmac object using the key and the message and the sha256 hashing algorithm
    h = hmac.new(key.encode(),message.encode(),hashlib.sha256)

    #return the hmac object
    truncated_h = h.digest()[:20];
    return int.from_bytes(truncated_h, byteorder="big")
    

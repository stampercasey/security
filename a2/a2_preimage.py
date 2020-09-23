import hashlib
import random
import string

def find_preimage(target, n):

    hexTarget = target.encode('hex')
    chars = string.printable
    randomStr = ""

    while (True):

        randomStr = "".join(random.choice(chars) for _ in range(8))
        digestedRandom = hashlib.sha256(randomStr).hexdigest()

        k = 0
        for i in range(2*n):
           if hexTarget[i] == digestedRandom[i]:
                k+=1
    
        if k == 2*n:
            break
    
    return randomStr
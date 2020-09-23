import hashlib
import random
import string

def find_collision(n):

    chars = string.printable
    hashDict = {}
    targetKey = ""
    m1 = ""

    while (True):

        m1 = "".join(random.choice(chars) for _ in range(8))
        digestedm1 = hashlib.sha256(m1).hexdigest()

        for key in hashDict:
            k = 0
            for i in range(2*n):
                if digestedm1[i] == hashDict[key][i]:
                    k+=1
            if k == 2*n:
                if digestedm1 == hashDict[key]:
                    continue
                else:
                    targetKey = key
                    break
        else:
            hashDict[m1] = digestedm1
            continue
       
        break

    return (m1, targetKey)
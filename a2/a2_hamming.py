import hashlib
import sys

def hammingdistance(hex1, hex2):
    x1 = hexToBinary(hex1)
    x2 = hexToBinary(hex2)
    length = 0
    distance = 0

    if len(x1) >= len(x2):
        length = len(x1)
    else:
        length = len(x2)

    while len(x1) - length != 0:
        x1 = "0" + x1

    while len(x2) - length != 0:
        x2 = "0" + x2
    
    for i in range(length):
        if x1[i] != x2[i]:
            distance+=1
    
    return distance

def hexToBinary(hex):
    x = int(hex, 16)
    bStr = ''
    while x > 0:
        bStr = str(x % 2) + bStr
        x = x >> 1
    return str(bStr)
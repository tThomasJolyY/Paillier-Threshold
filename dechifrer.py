import math
import json
from generatefunctions import calcbigpower
import sys

sys.setrecursionlimit(10000)

def dechiffrer(c,delta,ski,n):
    #print("je suis dans dechiffrer voici le chiffré:",c)
    pow = 2*delta*ski
    #print("je suis toujours dans déchiffrer, voici pow",pow)
    t = n**2
    ci = calcbigpower(c,pow,t)
    return ci

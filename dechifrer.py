import math
import json
from generatefunctions import calcbigpower
import sys

sys.setrecursionlimit(10000)

def dechiffrer(c,delta,ski,n):
    pow = 2*delta*ski
    t = n**2
    ci = calcbigpower(c,pow,t)
    return ci

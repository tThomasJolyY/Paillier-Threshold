import sys
import math
from generatefunctions import generate, init_votant
import json

"""
Initializes the public key and the secret keys according to the given arguments
"""

sys.setrecursionlimit(10000)

if len(sys.argv) == 4:
  nb_serv = int(sys.argv[1])
  t = int(sys.argv[2])
  candidats = int(sys.argv[3])

else:
  nb_serv = int(sys.argv[1])
  t = nb_serv -1
  candidats = int(sys.argv[2])
  
delta = math.factorial(nb_serv)

conf = {"nbserv":nb_serv,"t":t,"candidats":candidats,"delta":delta}

with open("globalConf.json","w") as write:
  json.dump(conf,write,indent=4)

#the two functions below will setup everything we need (public key, secret keys, verification keys and json files)
generate(nb_serv,t,delta)
init_votant(candidats)
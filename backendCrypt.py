import sys
import json
from chiffrer import chiffrer

"""
This file is used on the client side, when the user needs to crypt his message
"""

uid = sys.argv[1]
m = int(sys.argv[2])

with open("pubkey.json","r") as read_file:
  pubkey = json.load(read_file)

with open("globalConf.json","r") as read_file:
  conf = json.load(read_file)

#we cypher 1 for the pretender choosen by the user and 0 for all the others
for j in range(conf["candidats"]):
  if j == m:
    vote = 1
  else:
    vote = 0
  chiffrer(pubkey["g"],pubkey["n"],vote,uid,j)
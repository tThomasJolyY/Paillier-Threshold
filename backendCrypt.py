import sys
import json
from chiffrer import chiffrer

'''
Ce fichier est appelé coté client lorsque le votant chiffre son vote.
'''

uid = sys.argv[1]
m = int(sys.argv[2])

with open("pubkey.json","r") as read_file:
  pubkey = json.load(read_file)

with open("globalConf.json","r") as read_file:
  conf = json.load(read_file)

'''
Pour chaque candidat, on chiffre 1 si le candidat est celui pour lequel a voté le client,
et 0 sinon.
'''
for j in range(conf["candidats"]):
  if j == m:
    vote = 1
  else:
    vote = 0
  chiffrer(pubkey["g"],pubkey["n"],vote,uid,j)
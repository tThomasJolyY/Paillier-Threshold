from combine import decrypt
from homomorphe import getFinalCrypt
import json

with open("pubkey.json","r") as read_file:
    pubkey = json.load(read_file)

with open("globalConf.json","r") as read_file:
  conf = json.load(read_file)

with open("ci.json","r") as read_file:
  liste_ci = json.load(read_file)

with open("votes.json","r") as read_file:
  l_votes = json.load(read_file)

n2 = pubkey["n"]**2

resultats_vote = []

for i in range(conf["candidats"]):
    ci_candidati = []
    for j in range(conf["nbserv"]):
       ci_candidati.append(liste_ci[str(j)][i])
    finalc = getFinalCrypt(l_votes[i],n2)
    m = decrypt(ci_candidati,conf["delta"],pubkey,conf["nbserv"],finalc)
    print(m)
    resultats_vote.append(m)

#we write the results in a json file
with open("resultats.json","w") as write_file:
    json.dump(resultats_vote,write_file,indent=4)

import json
from homomorphe import getFinalCrypt
from dechifrer import dechiffrer
from combine import decrypt

"""
This file is used when the vote has ended and we need to compute the results
"""

#we get the pukbey, secretkeys and the global configuration from the json files
with open("pubkey.json","r") as read_file:
    pubkey = json.load(read_file)

with open("secretkeys.json","r") as read_file:
    secret_keys = json.load(read_file)

with open("globalConf.json","r") as read_file:
  conf = json.load(read_file)

filename = "votes.json"
with open(filename,"r") as read_file:
  l_votes = json.load(read_file)

resultats_vote = []

#we compute the results for each pretender
for i in range(conf["candidats"]):
    n2 = pubkey["n"]**2
    finalc = getFinalCrypt(l_votes[i],n2)

    liste_ci = []
    for j in range(1,conf["nbserv"]+1):
        liste_ci.append(dechiffrer(finalc,conf["delta"],secret_keys[str(j)],pubkey["n"]))

    with open("ci.json","w") as write_file:
        json.dump(liste_ci,write_file,indent=4)

    m = decrypt(liste_ci,conf["delta"],pubkey,conf["nbserv"],finalc)
    print(m)
    resultats_vote.append(m)

#we write the results in a json file
with open("resultats.json","w") as write_file:
    json.dump(resultats_vote,write_file,indent=4)
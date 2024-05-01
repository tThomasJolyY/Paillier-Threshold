from combine import decrypt
from homomorphe import getFinalCrypt

with open("globalConf.json","r") as read_file:
  conf = json.load(read_file)

with open("ci.json","r") as read_file:
  liste_ci = json.load(read_file)

for i in range(conf["candidats"]):
    finalc = getFinalCrypt(l_votes[i],n2)
    m = decrypt(liste_ci,conf["delta"],pubkey,conf["nbserv"],finalc)
    print(m)
    resultats_vote.append(m)

#we write the results in a json file
with open("resultats.json","w") as write_file:
    json.dump(resultats_vote,write_file,indent=4)

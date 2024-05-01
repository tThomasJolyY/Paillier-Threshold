import json
import sys
from homomorphe import getFinalCrypt
from dechifrer import dechiffrer

indice = sys.argv[1]

'''
Ce fichier est appelé sur les serveurs # serv central pour qu'ils
effectuent chacun leur déchifrement partiel
'''

'''
Je crois que y'a des trucs a modifier (genre on appelle les trucs pour calculer les ci
ici alors qu'en vrai il faudrait pas, faut récupérer ceux qui ont déja été calculé par les
serveurs.)
'''
with open("pubkey.json","r") as read_file:
    pubkey = json.load(read_file)

with open("secretkey.json","r") as read_file:
    secret_keys = json.load(read_file)

with open("globalConf.json","r") as read_file:
  conf = json.load(read_file)

with open("votes.json","r") as read_file:
  l_votes = json.load(read_file)

resultats_vote = []

n2 = pubkey["n"]**2
liste_ci = []

#we compute the results for each pretender
for i in range(conf["candidats"]):
    finalc = getFinalCrypt(l_votes[i],n2)
    liste_ci.append(dechiffrer(finalc,conf["delta"],secret_keys["1"],pubkey["n"]))

    #modifier ca pour que chaque serv ajoute son dechifré
with open("serveur"+str(indice)+"ci.json","w") as write_file:
  json.dump(liste_ci,write_file,indent=4)
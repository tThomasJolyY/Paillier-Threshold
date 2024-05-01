import os
import json

with open("globalConf.json","r") as read_file:
  conf = json.load(read_file)

liste_ci = {}

for i in range(conf["nbserv"]):
  with open("serveur"+str(i+1)+"/serveur"+str(i+1)+"ci.json","r") as read_file:
    ci = json.load(read_file)
  liste_ci[i] = ci

with open("ci.json","w") as write_file:
  json.dump(liste_ci,write_file,indent=4)
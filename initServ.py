import os
import json

with open("globalConf.json","r") as read_file:
  conf = json.load(read_file)

with open("secretkeys.json","r") as read_file:
    secret_keys = json.load(read_file)

for i in range(conf["nbserv"]):
  os.system("mkdir serveur"+str(i+1))
  with open("secretkey.json","w") as write:
    json.dump({"1":secret_keys[str(i+1)]},write,indent=4)
  os.system("mv secretkey.json serveur"+str(i+1))
  os.system("cp backendDecrypt.py serveur"+str(i+1))
  os.system("cp globalConf.json serveur"+str(i+1))
  os.system("cp votes.json serveur"+str(i+1))
  os.system("cp pubkey.json serveur"+str(i+1))
  os.system("cp homomorphe.py serveur"+str(i+1))
  os.system("cp dechifrer.py serveur"+str(i+1))
  os.system("cp generatefunctions.py serveur"+str(i+1))
  
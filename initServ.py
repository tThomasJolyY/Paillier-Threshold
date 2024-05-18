import os
import json
import shutil

with open("globalConf.json","r") as read_file:
  conf = json.load(read_file)

with open("secretkeys.json","r") as read_file:
    secret_keys = json.load(read_file)

for i in range(conf["nbserv"]):
  os.system("mkdir serveur"+str(i+1))
  with open("secretkey.json","w") as write:
    json.dump({"1":secret_keys[str(i+1)]},write,indent=4)
  shutil.copyfile("secretkey.json","serveur"+str(i+1)+"/secretkey.json")
  shutil.copyfile("backendDecrypt.py","serveur"+str(i+1)+"/backendDecrypt.py")
  shutil.copyfile("globalConf.json", "serveur"+str(i+1)+"/globalConf.json")
  shutil.copyfile("votes.json", "serveur"+str(i+1)+"/votes.json")
  shutil.copyfile("pubkey.json", "serveur"+str(i+1)+"/pubkey.json")
  shutil.copyfile("homomorphe.py", "serveur"+str(i+1)+"/homomorphe.py")
  shutil.copyfile("dechifrer.py", "serveur"+str(i+1)+"/dechifrer.py")
  shutil.copyfile("generatefunctions.py", "serveur"+str(i+1)+"/generatefunctions.py")
  os.remove("secretkey.json")
  
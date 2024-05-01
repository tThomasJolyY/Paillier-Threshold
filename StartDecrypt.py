import os
import json

with open("globalConf.json","r") as read_file:
  conf = json.load(read_file)

for i in range(conf["nbserv"]):
  os.system("cd serveur"+str(i+1))
  os.system("python serveur"+str(i+1)+"/backendDecrypt.py "+str(i+1))
  os.system("cd ../")
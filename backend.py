from generatefunctions import generate,init_votant
from chiffrer import chiffrer
from dechifrer import dechiffrer
from combine import decrypt
import sys
import json
import math
from sympy.ntheory.factor_ import totient 

sys.setrecursionlimit(10000)

nb_serv = 7
t = 3
delta = math.factorial(nb_serv)

generate(nb_serv,t)
init_votant()

m = 17
with open("pubkey.json","r") as read_file:
    pubkey = json.load(read_file)

phin = totient(pubkey["n"])
print("voici phi(n) = ",phin," et voici pgcd(n,phi(n)) = ",math.gcd(pubkey["n"],phin))
chiffrer(pubkey["g"],pubkey["n"],m,"0")

with open("votes.json","r") as read_file:
    l_votes = json.load(read_file)

print("le vote en question frere :",l_votes["0"])
c = l_votes["0"]

with open("secretkeys.json","r") as read_file:
    secret_keys = json.load(read_file)

print("liste sk_i = ",secret_keys)

liste_ci = []
for i in range(1,nb_serv+1):
    liste_ci.append(dechiffrer(c,delta,secret_keys[str(i)],pubkey["n"]))

print("Liste des ci = ",liste_ci)

with open("ci.json","w") as write_file:
    json.dump(liste_ci,write_file,indent=4)

decrypt(liste_ci,delta,pubkey,nb_serv,c)

import json

from generatefunctions import generateZn, calcbigpower

import sys

sys.setrecursionlimit(4096)

def chiffrer(g,n,m,uid,candidat):
    filename = "votes.json"
    x = generateZn(n)
    #x = 287
    #print("x = ",x)

    t = n**2
    gm = calcbigpower(g,m,t)
    xn = calcbigpower(x,n,t)
    c = (gm*xn)%t
    
    with open(filename,"r") as read_file:
        votes = json.load(read_file)
    
    votes[candidat][uid] = c

    with open(filename,"w") as write_file:
        json.dump(votes,write_file,indent=4)


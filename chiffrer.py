import json

from generatefunctions import generateZn, calcbigpower

import sys

sys.setrecursionlimit(4096)

def chiffrer(g,n,m,uid):
    x = generateZn(n)
    #x = 287
    #print("x = ",x)

    t = n**2
    gm = calcbigpower(g,m,t)
    xn = calcbigpower(x,n,t)
    c = (gm*xn)%t
    
    with open("votes.json","r") as read_file:
        votes = json.load(read_file)
    
    votes[uid] = c

    with open("votes.json","w") as write_file:
        json.dump(votes,write_file,indent=4)


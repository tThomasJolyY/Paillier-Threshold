from generatefunctions import calcbigpower,exp_func
import sys
import json
import math
from decimal import Decimal

sys.setrecursionlimit(1000000)

def usoj(delta,j,nbserv):
    restop = 1
    resbottom = 1
    for i in range(1,nbserv+1):
        if i!=j:
            restop = restop * (-i)
            resbottom = resbottom * (j-i)
    res = restop/resbottom            
    res = res * delta
    #print("je suis dans uso",j," = ",res)
    return int(res)

def lfunc(u,n):
    return (u-1)//n

def decrypt(s,delta,pubkey,nbserv,c=0):
    n = pubkey["n"]
    t = n**2
    res = 1
    for i in range(len(s)):
        pui = 2*usoj(delta,i+1,nbserv)
        #print("pow a l'étape ",i+1,"=",pui)
        #print("c",i+1,"=",s[i])
        #inter = calcbigpower(s[i],pui,t)
        inter = pow(s[i],pui,t)
        #print("pow avec usoj :",inter)
        #print("res de ci^pow = ",inter)
        res = res * inter % t
        #print("res de res * res d'avant =",res)
    #en dessous, calcul avec la dernière formule :
    #somme = 0
    #for i in range(len(s)):
    #    somme += usoj(delta,i+1,nbserv)*s[i]
    #print("voila la somme sympa dernière méthode :",somme)
    #pui = 4*delta*somme
    #res = calcbigpower(c,pui,t)
    #fin de la partie calcul somme
    #print("res pi = ",res)
    p1 = lfunc(res,n)
    #print("res de lfunc = ",p1)
    #print("on veut l'inverse de ",(4*pubkey["teta"]*delta**2))
    p2 = pow(4*pubkey["teta"]*(delta**2),-1,n)
    #p2 = (1/(4*pubkey["teta"]*(delta**2))) % n
    #print("on trouve = ",p2)
    m = (p1*p2)%n
    print("m:",m)
import math
import json
from generatefunctions import calcbigpower

def verification(c,delta,n2,v,liste_ci):
  #print("Voici le chiffré :",c)
  with open("secretkeys.json","r") as read_file:
    secret_keys = json.load(read_file)
  with open("vi.json","r") as read_file:
    liste_vi = json.load(read_file)

  c4d = pow(c,4*delta,n2)
  vd = pow(v,delta,n2)

  for i in range(len(liste_ci)):
    #print("je suis a l'étape ",i)
    ci = liste_ci[i]
    ci2 = pow(ci,2,n2)
    vi = liste_vi[i]
    ski = secret_keys[str(i+1)]
    #print("voici pow ",2*delta*ski)
    if calcbigpower(c4d,ski,n2) != ci2:
      print("La vérification n'est pas valide")
      return False
      #print("Egalité de ci pour i=",i)
    #else:
      #print("ntm le générateur pour i=",i)
      #print("Voici ci :",liste_ci[i])
      #print("voici ci recalculé :",pow(c,2*delta*ski,n2))

    if pow(vd,ski,n2) != vi:
      print("La verification n'est pas valide")
      return False
    #else:
    #  print("ntm la pute pour i=",i)
    return True
c1 = 1
c2 = 36
c3 = 1121


goal = 1191

upperlim = 20

mod = 1225

#for x in range(1,upperlim):
#    for y in range(1,upperlim):
#        for z in range(1,upperlim):
#            p1 = c1**(2*x)
#            p2 = c2**(2*y)
#            p3 = c3**(2*z)
#            res = (p1*p2*p3)%mod
#            if res == goal:
#                print("\nx = ",x,"\ny = ",y,"\nz = ",z)

def newusoj(j):
    res = 1
    for i in range(4):
        if i!=j:
            res = res * ((i)/(i-j))
    res = res * 6
    return res

def func_sk(x,liste_ai):
    val = 0
    for j in range(len(liste_ai)):
        val += liste_ai[j]*(x**j)
    return val

liste_ai = [78, 141, 144, 64]
s0 = func_sk(0,liste_ai)%1225

c0 = (703**(2*6*s0))%1225

liste_ci = [c0,c1,c2,c3]

final = 1
for i in range(4):
    res = 2 * int(newusoj(i))
    final = (final * (liste_ci[i]**res))
final = final%1225

teta = (9 * 8 * 6) % 35
teta2 = ((286**(6*13))-1)/35 % 35

print("teta : ",teta,"teta recalc :",teta)

final = final%1225
print(final%35)
l =int((final-1)/35)
print(l)
print(int(l*(1/4*(6**2)*teta))%35)


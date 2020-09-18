# -FORR3RR05DU

svar 1:
Binary talan er sett í lista.

summa=0

Ég nota forlubbu yfir i = 0 til lengdarinnar á tviendarkerfistölunni 
	Tek burt aftasta stafinn og margfalda með 2^i
	Svo legg ég það við summuna
Síðan prenta ég summuna.

 t_tala = list(input("sladu inn tviendatölu:"))
summa = 0
 
for i in range(len(t_tala)):
def summa(n):
    if(n>=1):
      temp = summa(n-1) + n
      print(temp)
      return temp
    else:
        return 0
 
summa(6)
    stafur = t_tala.pop()
    if stafur == '1':
        summa = summa + pow(2, i)
print( summa)

svar 2:
def summa(n):
    if(n>=1):
      return summa(n-1) + pow(n,2)
    else:
        return 0
 
    
print(summa(5))

Svar:
55

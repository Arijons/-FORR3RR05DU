
#dæmi 1
 t_tala = list(input("sladu inn tviendatölu:"))
summa = 0

for i in range(len(t_tala)):
	stafur = t_tala.pop()
	if stafur == '1':
		summa = summa + pow(2, i)
print( summa) 

#dæmi 2
 def summa(n):
    if(n>=1):
      return summa(n-1) + pow(n,2)
    else:
        return 0

    
print(summa(5)) 

#dæmi 3
 def summa(n):
    if(n>=1):
      temp = summa(n-1) + n
      print(temp)
      return temp
    else:
        return 0

    

    
summa(6) 

#dæmi 4

 def thv_summa(tala):
    if len(tala) > 0:      
        tala,stafur = tala[:-1], tala[-1]
        return thv_summa(tala) + int(stafur)
    else:
        return 0

print(thv_summa('6789')) 


#5

def samnefnari(a,b): 
	if(b==0): 
		return a 
	else: 
		return samnefnari(b,a%b) 

a = 60
b= 48


print ("samnefnarinn er:")
print (samnefnari(12,8)) 
print (samnefnari(13,3))
print(samnefnari(60,12))
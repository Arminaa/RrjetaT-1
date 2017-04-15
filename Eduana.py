import datetime
from random import randint
import math
from pickle import INT
from json.decoder import NaN


llojiKerkeses=input("Ju lutem shenoni kerkesen tuaj:")

if llojiKerkeses=='IP':
    pergjigjja=addr
    #per udp-Serverin
    #pergjigjja=clientAddress

elif llojiKerkeses=='PORT':
    pergjigjja=serverPort

elif llojiKerkeses=='ZANORE':
    pergjigjja="P"

elif llojiKerkeses=='PRINTO':
    
    kerkesa="U"
    pergjigjja=kerkesa
    print(pergjigjja)

elif llojiKerkeses=='TIME':
    pergjigjja="P"

elif llojiKerkeses=='KENO':
     i=1
     fund=81
     while i <= fund:
          pergjigjja = randint(0,80)
          print(pergjigjja)
          i=i+1
         
elif llojiKerkeses=='KONVERTO':
    choose=int(input("C->F 1| C->K 2| K->F 3|K->C 4| F->C 5| F->K 6| P->K 7| K->P 8| \n"))
    temp=(input("Jepni vleren:\n"))
    def isNaN(x):
       return str(x) == str(1e400*0)
    if temp!= NaN:
        isNaN(temp)
    else:
    


        if choose==1:
            print(float((temp * 9/5) + 32))
        elif choose==2:
            print(float((temp - 32) * 5/9))
        elif choose==3:
            print(float((temp - 273.15) * 9/5 + 32))
        elif choose==4:
            print(float(temp - 273.15))
        elif choose==5:
            print(float((temp - 32) * 5/9))
        elif choose==6:
            print(float((temp - 32) * 5/9 + 273.15))
        elif choose==7:
            print(float(temp*(1/2.2)))
        elif choose==7:
            print(float(temp*2.2))

        else:
            print("E hyra jo valide")


elif llojiKerkeses=='FAKTORIEL':
    n=int(input("Te jepet nje numer pozitiv: "))
    print(math.factorial(n))

  

elif llojiKerkeses=='HOST':
    pergjigjja="P"

else:
    pergjigjja="Invalid"




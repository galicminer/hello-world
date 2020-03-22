import math
n=int(input("ingrese numero: "))
if ((n%2)==1):
    print("Weird")
elif (n<=5) and (n>=2):
    print("Not Weird")
elif (n<=20) and (n>=6):
    print("Weird")
elif (n>20):
    print("Not Weird")

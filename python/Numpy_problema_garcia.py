import numpy as np
n=int(input())
arr=np.zeros(n)
for i in range(n):
    if i==0:
        arr[i]=0
    else:
        arr[i]=arr[i-1]+2*(i-1)+1
print(arr)
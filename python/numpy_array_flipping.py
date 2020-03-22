import numpy as np
def arrays(arr):
    tamano=arr.size
    new=np.zeros(tamano)
    for i in range(tamano):
        new[tamano-i-1]=arr[i]
    return new

c=np.array(input().strip().split(' '),float)
print(arrays(c))

import numpy as np

line1 = np.array((input().strip().split(' ')),int)
matr=np.zeros((line1[0],line1[1]),int)
for n in range(line1[0]):
    line2=np.array((input().strip().split(' ')),int)
    for m in range(line1[1]):
        matr[n][m]=line2[m]
print (np.transpose(matr))
print (matr.flatten())
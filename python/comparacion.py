n=int(input())
arr=list(map(int,input().split()))
mayor=0
mayordis=mayor
dist=[]
for i in arr:
    if i>mayor:
        mayor=i
for m in arr:
    distan=mayor-m
    dist.append(distan)
for p in dist:
    if p>menordis:
        menordis=p
print(arr[dist.index(mayordis)])
    
    
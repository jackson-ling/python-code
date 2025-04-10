li=[9,8,7,5,4,6,2,3,1]
n=len(li)
for i in range(0,n-1):
    for j in range(i+1,n):
        if li[i]>li[j]:
            li[i],li[j]=li[j],li[i]
print(li)
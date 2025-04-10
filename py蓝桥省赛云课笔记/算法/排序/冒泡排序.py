li=[9,8,7,5,4,6,2,3,1]
n=len(li)
for i in range(0,n-1):
    for j in range(0,n-1-i):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
print(li)
li.sort() #是一个过程，不可以直接打印这个对象，否则结果值就是None
print(li)
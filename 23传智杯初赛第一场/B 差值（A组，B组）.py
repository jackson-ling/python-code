a=int(input())
li=[int(i) for i in input().split()]
li1=[]
li.sort()
for i in range(1,len(li)):
     minx=li[i]-li[i-1]
     li1.append(minx)
print(min(li1))


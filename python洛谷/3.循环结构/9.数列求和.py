#方法一
n=int(input())
li=[int(i) for i in range(1,n+1)]
tot=sum(li)
print(tot)

#方法二
n=int(input())
tot=0
for i in range(1,n+1):
    tot+=i
print(tot)
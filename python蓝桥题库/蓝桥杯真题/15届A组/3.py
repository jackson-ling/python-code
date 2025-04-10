a=int(input())
li=[int(i) for i in input().split()]
li1=[int(i) for i in range(100)]
cnt=0
ans=0
for i in li:
    for j in range(len(li1)):
        ans+=li1[j]
        if i==ans:
            cnt+=1
            continue
print(cnt)



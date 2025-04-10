ls=[int(i) for i in input().split()]
ls2=[i for i in input()]
ls=sorted(ls)
ls3=[]
start='A'
for i in range(3):
    ls3.append([start,ls[i]])
    start=chr(ord(start)+1)

for i in range(len(ls2)):
    for j in range(len(ls3)):
        if ls2[i]==ls3[j][0]:
            print(ls3[j][1],end=' ')

li1=[i for i in input()]
li2=[i for i in input()]
for i in li1:
    for j in li2:
        if j in li1:
            li1.remove(j)
for i in li1:
    print(i,end='')
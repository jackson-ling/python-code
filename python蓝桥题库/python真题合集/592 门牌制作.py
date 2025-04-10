cnt=0
for i in range(1,2021):
    for j in str(i):
        if j=='2':
            cnt+=1
print(cnt)

# 其他方法（巧妙的利用count）

print("".join([str(i) for i in range(1, 2021)]).count("2"))



b=0
for i in range (1,2021):
  a=str(i).count('2')
  b+=a
print(b)


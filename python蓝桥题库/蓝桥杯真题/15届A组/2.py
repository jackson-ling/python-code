a=0
b=0
cnt=0
n=0
for i in range(2024041331404202):
    n+=1
    a+=n
    b*=n
    if (a-b)%100==0:
        cnt+=1
print(cnt)
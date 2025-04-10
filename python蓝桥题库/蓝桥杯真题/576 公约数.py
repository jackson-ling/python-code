cnt=0
for i in range(1,3031):
    if 2020%i==0 and 3030%i==0:
        cnt+=1
print(cnt)
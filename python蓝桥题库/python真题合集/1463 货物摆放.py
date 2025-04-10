n=int(input())
tot=0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i*j*k==n:
                tot+=1
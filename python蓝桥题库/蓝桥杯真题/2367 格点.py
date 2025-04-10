cnt=0
for x in range(1,2022):
    for y in range(1,2022):
        if x*y<=2021:
            cnt+=1
print(cnt)
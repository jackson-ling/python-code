#本题目不难，但是没做出来，重点放在审题
cnt=0
for i in range(4,2021):
    for j in range(2,i):
        if i%j==0:
            cnt+=1
            break   #重点在这，只要找到就说明还有其他因子，无论是几个都符合和数的定义
print(cnt)
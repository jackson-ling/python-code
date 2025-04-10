a=int(input())
cnt=1
while True:
    if a==1:
        print(cnt)
        break
    a=int(a/2)
    cnt+=1
#向下取整：
# 1.int（）
# 2.math.floor(变量)
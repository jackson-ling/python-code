a,b,c,d=map(int ,input() .split())
# print(a,b,c,d)
#从a小时b分钟游到c小时d分钟



#测试：假设重两点10游到三点20，游了一个小时10分钟
if (c-a>=0)and(d-b>=0):
    print(c-a,d-b)
elif (c-a>=0)and(d-b<=0):
    e=(c-a-1)
    f=60+d-b
    print(e,f)








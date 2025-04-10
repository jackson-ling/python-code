#定义一个进制转换函数
def fuc(x,n):
    ans=0
    while x>0:
        ans+=x%n
        x//=n  # 注意：只取整数位，区别C语言，python的除法结果自带小数
    return ans
tot=0
for i in range(1,2025):  # 注意左闭右开
    if fuc(i,2)==fuc(i,4):
        tot+=1
print(tot)

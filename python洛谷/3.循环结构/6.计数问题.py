n,x=[i for i in input().split()]#这里接收的是字符串类型
cnt=0
for i in range(1,int(n)+1):
    if x in str(i):
        cnt+=list(str(i)).count(x)#运用列表统计方法count（）函数
print(cnt)
#注意，要把数据添加到列表，应该是一个可迭代序列，此处把数据类型转成字符窜类型
# 报错：'int' object is not iterable
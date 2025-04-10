"""
随机取10次 1 到 10 范围内的整数数据, 添加到列表
"""
# 要使用到python内置模块
# random （不需要下载的）
import random
# print(random.randint(1,10))   #  随机从1到10取一个整数 左右都是闭区间

# 通过循环去控制次数

list1 = []
for i in range(10): #0123456789 随机取10次
    list1.append(random.randint(1,10))
print(list1)


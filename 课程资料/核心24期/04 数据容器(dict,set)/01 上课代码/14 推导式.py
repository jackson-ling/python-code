# 为什么没有元组的推导式呢?
# 1.元祖是一个不可变的数据类型
# 按照自己的需要去使用推导式


# 用于快速去生成一个列表
# 列表推导式
result = [i for i in range(0, 7)]
print(result)
# 可以分为2个部分
# 第一部分
# for i in range(0, 7):
#     print(i)
# # 第二部分  是将遍历出来的每一个数据 作为列表的元素
# # [0, 1, 2, 3, 4, 5, 6] 就相当于把每一个数据添加到空的列表里面去 然后去组成列表返回


# 字典推导式
result1 = {i + 1: i for i in range(8)}
print(result1)


# 结合推导式 集合里面是一个一个单独的元素
result2 = {i * 2 for i in range(8)}
print(result2)


#生成同一种数据的列表推导式
l=int(input())
a=[1 for i in range(l+1)]#循环数据是1，用循环遍历表示循环L次，生成长度为L+1，每个数据为1的列表
print(a)
#运行结果
# 3
# [1, 1, 1, 1]

# 推导式主要用于节省步骤




import copy
# a = [1,3,4,5]
# b = copy.copy(a)  # 浅拷贝 创建另一个对象
#
# a[1] = 25
# print(a)
# print(b)
#
#
#
# # # id地址是不一样的表示引用的不是同一个对象  也就是说开辟2个不同的内存空间
# print(id(a))
# print(id(b))

# 有一个限制的  浅拷贝只适用于 一维维度 多维没有作用

a1 = [1,3,[1,4,5]]
b = copy.copy(a1)
a1[2][0] = 25
print(a1)
print(b)
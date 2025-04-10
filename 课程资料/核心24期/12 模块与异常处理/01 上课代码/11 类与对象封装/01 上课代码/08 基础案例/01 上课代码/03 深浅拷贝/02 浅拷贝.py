# 浅拷贝 只拷贝父对象，不会拷贝对象的内部的子对象
from copy import copy
# a = [1,2,3,4,5]
# b = copy(a)
#
# a[0] = 5
# print(a)
# print(b)
# print(id(a))
# print(id(b))

# 重点
# 针对列表的嵌套,浅拷贝是无能为力的  用于一维维度
# a = [1,2,[1,2,3],3,4,5]
# b = copy(a)
#
# a[2][0] = 6
# print(a)
# print(b)







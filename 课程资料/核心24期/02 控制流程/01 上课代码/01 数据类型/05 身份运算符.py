# x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
# x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False

# a = 1
# b = 2

# 通过id函数进行判断 如果id函数打印的结果相同 那么就表示他们引用的是同一个对象
# print(id(a))
# print(id(b))
# print(a is b)

a = 1
b = 1
print(id(a))
print(id(b))
print(a is b)
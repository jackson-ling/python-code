# # 需求：有变量`a = 10`和`b = 20`，交换两个变量的值。
# a = 10
# b = 20
# a = 20
# b = 10
# print(a)
# print(b)
# 这个方法非常的不建议大家这么写 变量的覆盖重新赋值可能会有影响

# # 通过第三者的介入

'''区别C语言，python不像C语言可以定义变量就能用，在python中变量要有值才可以，c = None是精髓'''

# c = None #  None就是一个空的对象 相当于一个空的瓶子
# c = a # 将a里面的数据保存到c里面
# a = b # 将b的数据保存到a里面去
# # b = c # c保存着a的值
# print(a)
# print(b)

# 方法二
# 等效替换
a,b= 12,25
print(a)
print(b)

# 交换数据（一一对应）
a,b = b,a
print(a)
print(b)


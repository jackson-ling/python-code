# 无参数
# fun = lambda : 100
# print(fun())

# 一个参数
# fun1 = lambda a: a
# print(fun1(2))


# 默认参数 (是在定义函数的时候就已经给参数进行了关键字的赋值)
# fun2 = lambda a, b, c=100: a + b + c
# print(fun2(1,4,5))  # 传递过去的值会覆盖掉默认参数的值  别人有的就用别人
# print(fun2(1,5))    # 别人有的就用别人


# 位置参数
# fun3 = lambda a, b: a - b
# print(fun3(9, 6))


# # 关键字参数
# fun4 = lambda a, b: a - b
# print(fun4(a=4, b=7))

# 位置和关键字2者混用
# 位置参数永远在关键字参数的前面(一定要记清楚)
# fun5 =  lambda a, b, c: a - b + c
# print(fun5(1,5,c=5))

# 可变参数 #args  用于接受位置参数
# fun6 = lambda *args : args
# print(fun6(1,25,56,56,4,576)) # 返回的是一个元组
#
# # 可变参数：**kwargs  用于接受关键字参数
# fun6 = lambda **kwargs : kwargs
# print(fun6(a=6,b=9,c=7))   # 返回的字典类型
#
# # 进行混用 要带括号
fun8 = lambda *args,**kwargs:(args,kwargs)
print(fun8(1,4,5,a=5,b=7))  #一起返回



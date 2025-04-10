# -*- coding: utf-8 -*-
"""
定义一个函数，对传入未知个长度的内容进行求和并且返回
# 不定长参数

传入的内容如下(print里面的东西)

"""
# 对于未知长度的数据 不定长参数   args(用于接受位置参数) kwargs(关键字参数)
# print(1,2,3,4,5,a=6,b=7,c=8) 位置参数  关键字参数 args kwargs

"""自己在下方编写代码实现功能"""
# 定义参数还是调用函数的时候去传递参数 位置参数永远在关键字参数的前面
def func(*args,**kwargs):
    # print(args)     # 返回的是一个元组类型
    # print(type(args))
    total = 0 # 是为了初始化一个变量 方便后面的累加求和
    for i in args:
        # print(i)
        total += i # 等效于 total = total + i(赋值运算)
        # print(total) # print写在循环里面 打印的是相加过程
    # print(total) # 打印的是最终结果
    # print(kwargs)     # 返回的是一个字典
    # print(type(kwargs))
    a1 = 0
    for j in kwargs.values(): # 遍历字典的每一个值
       a1 += j
    # print(total) # args 和 kwargs一起的结果
    total1 = total + a1
    print(total1)
    return total1 # 通过return将函数内部的结果返回给函数外部 实现内外的数据共享

# 调用函数
print(func(1,2,3,4,5,a=6,b=7,c=8))

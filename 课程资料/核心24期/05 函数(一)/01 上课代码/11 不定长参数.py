"""
我需要统计班级中每个人的成绩总和
(我先不知道这个班到底有多少人)
"""


# 假设这个班有4个 不止4个      这个时候有多少个学生我的参数就要写多少个     肯定非常麻烦
# def get_num(res,res1,res2,res3):
#     total = res + res1 + res2 + res3
#     # 我什么情况要需要去写return
#     # 根据自己题目的要求而定的(如果函数外部需要用到函数内的数据,这个时候就需要写)根据情况而定
#     return total # 将数据返回给函数外部 实现内外的数据共享
#
# # 调用函数 执行代码逻辑
# print(get_num(80,84,85,86))
#
# *args 不定长参数 接受所有传进来的位置参数
# def get_num(*args):  # 作为参数* 必须要写
#     print(args)  # 变为变量打印的时候* 不需要写的
#     print(type(args))  # 接受位置参数 返回的是元组类型
#     # 讲数据进行累计求和
#     total = 0  # 用于后面累计求和
#     for i in args:
#         total += i # 等效于 total = total + i
#     return total
# # 调用函数 执行代码逻辑
# print(get_num(80, 84, 85, 86,85,84,87,87,85,87,85))


# # ** kwargs   接受所有传进来的关键字参数
# def get_num(**kwargs):  # 作为参数* 必须要写
#    print(kwargs)
#    print(type(kwargs)) # 返回值是字典类型数据
#    total = 0
#    for i in kwargs.values(): # 遍历字典的值
#        total += i
#    return total    # 将数据返回给函数外部 实现内外的数据共享

# print(get_num(a=9,b=6,c=7,d=8))


# 需求 求2个数的最大值

# # input 默认返回的是str类型
# a = int(input('请输入你的第一个数:'))
# b = int(input('请输入你的第二个数:'))

#
# # 大小的判断 针对数值类型
# if a > b:
#     num_max = a
# else:
#     num_max = a


# print(num_max)

# 三元运算又叫三目运算符
# 如果if后面的表达式布尔结果是True哪么就返回if左边的值,反之则返回else右边的值
# num_max = a if a > b else b
# print(num_max)

# 使用lambda去简化
# 只能写简单的函数逻辑, 稍微复杂一点的函数逻辑都不支持匿名函数
fun = lambda a,b: a if a > b else b
print(fun(18,114))
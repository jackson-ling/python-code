"""
把列表中所有人名的*去掉,比方: Tenc*ent-->  Tencent  replace
"""
name = ['Tenc*ent', 'Zhi*hu', 'Bai*du']

# 代码中要用到lambda函数
# lambda是为了去简化我们的函数逻辑(只能支持一些简单的函数逻辑)

# map(func, lst)，将传入的函数变量func作用到lst变量的每个元素中，并将结果组成新的列表

# def func(x):
#     # print(x)
#     s = x.replace('*','')
#     print(s)
#     return s # 实现函数内外的数据共享
#
# result = map(func,name) # map函数会默认去遍历序列 并且把遍历出来的元素一个个传递给对应的函数
# print(list(result))

# # 使用lambda进行简化
# result1 = map(lambda x:x.replace('*',''),name)
# print(list(result1))

# 方法二
# list1 = []
# for i in name:
#     s = i.replace('*','')
#     list1.append(s)
# print(list1)












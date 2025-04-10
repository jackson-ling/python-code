"""for 遍历"""
# 可迭代对象 str  list 字典等等
# for it in 'python': # 就是把字符串的每一个字符赋值i 然后在交给print打印
#     print(it)
#
# for i in [1,3,4,5]:
#     print(i)


# range函数

# range(start, stop[, step])

# - start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
# - stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
# - step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)


"""
    range(起始值, 结束值, 步长)
"""
# 步长不写默认是1
# 他是一个左闭右开区间
# print(range(0,9))
# print(list(range(0,9)))
#
# # 起始值不写 默认从0开始
# print(range(9))
# print(list(range(9)))



# 步长
# 步长为负数  从大到小
# 步长为正数  从小到大
print(list(range(0,6)))
# # print(list(range(0,6,-2)))
# print(list(range(0,6,2)))
print(list(range(9,2,-2)))


# # for 和 range的搭配使用
# for i in range(6):
#     print(i)



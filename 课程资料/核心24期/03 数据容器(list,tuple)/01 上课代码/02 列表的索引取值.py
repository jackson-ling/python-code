name_list = ['正心', '丸子', '自游', '巳月', '泽言','山禾',7,9]

# 取泽言的名字
# 顺序取值  从左往右
print(name_list[4])
# 逆序取值 从右往左
print(name_list[-2])

# 思考一个问题
# 去列表中取数据的，他的数据类型会不会发生变化
# 列表里面的数据是什么类型存进去那么取出来就是什么类型
# 数据容器只是对数据提供一个临时的保存场所，不会改变数据的任何性质
print(name_list[-1])
print(type(name_list[-1]))

"""重点错误"""
# # 取值超出了最大索引直接报错
# # IndexError: list index out of range
# print(name_list[25])


# 索引取值是序列特有的方法
# 字符串也是有下表索引的和列表保持一致 超出索引也是会报错的
# a1 = 'python'
# print(a1[25])




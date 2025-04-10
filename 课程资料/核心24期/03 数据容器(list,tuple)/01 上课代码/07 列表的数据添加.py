# append()：列表结尾追加数据。
# 列表序列.append(数据)
name_list = ['正心', '丸子', '自游', '巳月', '泽言']
# a = name_list.append('山禾') # 只是一个添加过程 没有返回值 才会打印 None
# print(a)
#
#
# """所有的列表变化调用的方法, 都是基于列表本身操作"""
# print(name_list)
# print(name_list.append('山禾'))   #返回值None
#
# name_list.append('山禾1','山禾2') # append方法每一次只能够添加一个参数
# name_list.append([1,2,3,4,5])   # 如果添加的是一个序列那么就是整体添加
# print(name_list)
# #
# # # 数值类型可以添加成功
# name_list.append(2)
# print(name_list)
#
# name_list.append('努力学python')
# print(name_list)

# extend()：列表结尾追加数据 如果数据是一个序列，则将这个序列的数据逐一添加到列表
 # # 列表序列.extend(数据)
#
#
name_list1 = ['正心', '丸子', '自游', '巳月', '泽言']
# print(name_list1.extend('山禾'))   #extend没有返回值  则将这个序列的数据逐一添加到列表
# # #
# print(name_list1)
# name_list1.extend([1,2,3,4])   # 则将这个序列的数据逐一添加到列表
# print(name_list1)
# name_list.extend([1,2,3])
# print(name_list)

# # extend()只能添加一个序列  数值类型不是一个序列  数值类型不是序列  'int' object is not iterable
# name_list1.extend(6)
# print(name_list1)
# # # 嵌套的列表
# name_list1.extend([[1,2,3,4,5]])# 嵌套列表会剥离最外面一层然后在添加 （先通过for循环遍历，然后在添加）
# name_list1.extend([1,2,3,4,5])
# print(name_list1)


# insert()：指定位置新增数据。
# 列表序列.insert(位置下标(索引), 数据)
#
name_list2 = ['正心', '丸子', '自游', '巳月', '泽言']
print(name_list2.insert(2,'山禾'))
print(name_list2)







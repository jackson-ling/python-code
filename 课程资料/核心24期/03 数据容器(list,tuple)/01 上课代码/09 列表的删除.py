# # # pop()：删除指定下标的数据(默认为最后一个)，并返回该数据
# # 列表序列.pop(下标)
# name_list1 = ['山禾', '丸子', '自游', '巳月', '泽言']
# name_list1.pop() # 删除指定下标的数据(默认为最后一个)，并返回该数据
# #                         # 后面需要用删除的数据 就可以直接用变量接收
# print(name_list1)
# # # """所有的列表变化调用的方法, 都是基于列表本身操作"""
# print(name_list1.pop(1))
# print(name_list1)
#
# # # 列表长度实在时刻发生变化
# print(name_list1.pop(2))
# print(name_list1)
#
# # 如果索引不存在  报错
# print(name_list1.pop(14))   # pop index out of range
# print(name_list1)



# remove()：移除列表中某个数据的第一个匹配项。
# # 列表序列.remove(数据)
name_list2 = ['山禾', '泽言','丸子', '自游', '巳月', '泽言']
print(name_list2.remove('泽言')) #  没有返回值的 指定数据删除
print(name_list2)
#
# name_list2.remove('泽言')    # 有多个一样的删除第一个
# print(name_list2)
#
# # 如果数据不存在  list.remove(x): x not in list 报错
# name_list2.remove('山禾1')
# print(name_list2)


# del 删除 指定索引在进行删除
# name_list = ['正心', '丸子', '自游', '巳月', '泽言']
# del name_list[3]
# print(name_list)
# del name_list         # 直接把变量定义给抹出了 就相当于这个变量出来没有被赋值过
# print(name_list)





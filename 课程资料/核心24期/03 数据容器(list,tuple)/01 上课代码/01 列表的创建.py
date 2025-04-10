# 变量名 = []   一定要是英文输入法       变量名 要符合标识符的命名规则

# list1 = []   #  创建了一个空列表  <class 'list'>
# print(type(list1))

# 列表里面的每一个数据都要使用英文状态下的逗号隔开 print    input
#  在python里面列表是可以存储所有python对象的
# list2 = [2,2.5,'python',True,False,print]
# print(list2)


# 易错点1
# 1.在后续变量的命名的时候, 千万不要用类型的关键字命名（int float str list........）
# 这种命名 禁止使用
# list
# list = [1,2,3,4,5]
# print(list)
# 因为这些关键字在python底层中有特殊作用 如果被引用了可能会发生底层的冲突 一定不要去这么做


# 易错点2
name1 = [1,45,25]
b = str(name1)
print(b)
# 使用type去打印一下b的类型
# 不能看他的一个表面  要使用type进行打印
print(type(b))

# 一定要注意数据类型, 根据不同的数据类型在python操作不同
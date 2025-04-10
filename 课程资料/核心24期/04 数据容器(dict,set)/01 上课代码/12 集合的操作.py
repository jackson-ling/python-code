# 根据遇到的问题去使用不同的容器 set可以去重
# 集合添加数据
# add()
set1 = {1,3,4,5,6}

# print(set1.add(5)) # 自动去重
# print(set1)

 # update(), 追加的数据是序列
set1.update('python')  #逐个取出在添加
print(set1)

set1.update([1,4,56])
print(set1)

# set1.update(25) # 数值类型不是序列  不能追加的
# print(set1)



# 重点
# 字典的键和值分别代表一个哈希值 集合只有一个哈希值 (只能去合并第一个哈希值)    做一个了解
set1.update({'name':'泽言'}) #  只会合并字典的一个键(合并是哈希值) 记住就好了
print(set1)



# 集合的删除
# remove()，删除集合中的指定数据，如果数据不存在则报错。
# set5 = {1,5,6,7,87,7} # 自动去重 实际上只有1个7
# # print(set5.remove(7))
# # print(set5)
#
#
# # 如果数据不存在则报错。
# print(set5.remove(25))
# print(set5)

# # discard()，删除集合中的指定数据，如果数据不存在也不会报错。
set5 = {1,5,6,7,87,7} # 自动去重 实际上只有1个7
# set5.discard(5)
# print(set5)

# 如果数据不存在  会返回原有的数据
set5.discard(78)
print(set5)
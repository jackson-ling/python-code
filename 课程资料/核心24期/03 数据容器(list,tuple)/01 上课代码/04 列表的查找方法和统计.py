# index()：返回指定数据所在位置的索引
# 列表序列.index(数据)
list1 = [41, 2, 1111, 100, 6, 2,5]
# print(list1.index(41))
# print(list1.index(2))  #  如果列表里面有多个一样的数据那么他会返回第一个下标索引,找到就结束
#
# print(list1.index(26))    # 数据不存在直接报错

# 如果列表内容 不定，只想取倒数第2个，怎么办？
# list1 = ['泽言',12,'男']
# print(list1[0])

# list1 = [12,'男','泽言',1,3,4,5,6]
# a = list1.index('泽言') # 返回指定数据所在位置的索引
# print(list1[a]) # 不管这个数据的位置怎么变 我都可以取到



# count()：统计指定数据在当前列表中出现的次数。
# print(list1.count(41))
# print(list1.count(2))
#
# print(list1.count(89))  # 统计没有的数据返回0次 不会报错



# len()：访问列表长度，即列表中数据的个数。
# 即列表中数据的个数。而不是索引
print(len(list1))

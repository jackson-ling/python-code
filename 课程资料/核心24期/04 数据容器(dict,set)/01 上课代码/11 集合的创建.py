"""
字典 里面是一个一个键值对
{}   区分字典, 没有键值对, 里面只有单个数据

<class 'set'>
            数据会默认自动去重
            集合是无序 : 每一次打印集合 在控制台的输出可能是不一样的
            他是没有索引和下标 不能通过下表索引去进行取值的


"""

set1 = {1,3,4,5,5,4} # 自动去重
print(type(set1))
print(set1)

# for 循环遍历取值
for i in set1:
    print(i)



# 先强转在取值
set2 = list(set1)
print(set2)

# 然后在转回来就可以了 也是一种方法

# 我现在实在创建字典还是集合?  是创建字典
set11 = {}
print(type(set11))


# 如果去创建一个空集合
set12 = set()
print(type(set12))



# filter(func, lst)函数用于过滤序列, 过滤掉不符合条件的元素, 返回一个 filter 对象。
# 如果要转换为列表, 可以使用 list() 来转换。

list1 = [1, 4, 5, 6, 7]


# def fun1(x):
#     # 这个过滤规则你是可以根据情况自己去定的
#     # 5 % 2 = 2.....1
#     return x % 2 == 0 # 筛选的就是偶数 过滤数据
#
# result = filter(fun1,list1)   # 会默认把序列的元素全部遍历 再把数据传递给形式参数x进行接受x(随便定义的)
# print(list(result))

# lambda进行简化

result1 = filter(lambda x:x % 2 == 0,list1)
print(list(result1))
# enumerate()函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
# 同时列出数据和数据下标，一般用在 for 循环当中。

list1 = ['a','b','c','d']
print(enumerate(list1))
print(list(enumerate(list1)))   # 返回一个列表包含元组的数据 元组的内容是下标和它对应数据


# for i in enumerate(list1):
#     print(i)


# 二次遍历
for i ,j in enumerate(list1):
    print(i,j)


# 这个方法可以搭配索引找数据去使用
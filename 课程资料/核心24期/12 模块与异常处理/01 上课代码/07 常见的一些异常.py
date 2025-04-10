# print(name)    # 先赋值声明后使用    变量被赋值了才会被创建
# # """
# #     NameError: name 'name' is not defined
# #     名称错误：name 没有被定义
# # """


# print(10/0)  # 在数学上分子不能为0的 在python里面也是同样的
# # """
# #     ZeroDivisionError: division by zero
# #     除零错误：任何数值被零除都会导致ZeroDivisionError错误
# # """


# a = [1,2,3,4]
# print(a[25])  # 超出了最大索引
# # """
# #     IndexError: list index out of range
# #     索引错误：使用一个超出范围的值索引时引发
# # """

dict1 = {
    'name':'泽言',
    'age' : 25
}
#
# print(dict1['kk'])

# get 防止键不存在而报错的方法
print(dict1.get('kk')) # None

"""
    KeyError: 'age'
    键错误：该字典没有这个键引发的报错
"""
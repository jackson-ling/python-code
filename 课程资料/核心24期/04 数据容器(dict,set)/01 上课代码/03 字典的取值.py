# 不能使用关键字去命名变量(str int list dict....)
# 字典取值是通过键去获取到他的值  (所以说我们的键必须唯一)
dict1 = {
    'name':'泽言',
    'age':25,
    '职业':'python讲师'

}
# print(dict1["name"])  #  字典可单可双  但是json数据一定要是双引号
# print(dict1['age'])

# 2种取值方法
# 取一个不存在的键  键不存在直接报错
# # print(dict1['kk'])
# print(dict1.get('name'))
# # get() 防止取到一个不存在的键而报错  不会报错 返回了None 由于它没有返回值的原因
#
# print(dict1.get('kk'))

# 字典本身的一些取值方法(一定要去记一下后面会用的)
"""keys()"""
print(dict1.keys()) # 取字典里面的所有键 返回的是一个对象
print(list(dict1.keys())) #通过list强转看对象里面的内容

"""values"""  # 返回字典的所有值
# print(dict1.values()) # 取字典里面的所有值 返回的是一个对象
# print(list(dict1.values())) #通过list强转看对象里面的内容


"""items"""
# print(dict1.items())
# print(list(dict1.items())) # 返回的是列表里面嵌套着多个元组

# 取python讲师
# print(list(dict1.items())[2][1])


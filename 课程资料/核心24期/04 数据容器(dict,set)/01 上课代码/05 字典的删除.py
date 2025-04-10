dict1 = {
    'name':'泽言',
    'age':25,
    '职业':'python讲师'
}
# 如果是强转的话保留是键
print(list(dict1))
# dict1['age1'] = '' # 空字符
# print(dict1)
# # del() / del：指定键, 删除字典中键值对
# del dict1['name']
# print(dict1)

# del dict1           # del直接把这个字典的声明给抹除了  我从来没有存在过一样
# print
#

# pop 方法

# 用于获取指定“键”的值，并将这个“键-值”对从字典中移除。
# # 键和值是一起存在的 同生共死 要通过键去删除整个键值对  没有什么单独删除值 删除键这么一说的
# 字典里面都是一个一个键值对数据
# print(dict1.pop('name'))  # 他也是有返回值 返回被删除数据的值

# # 如果删除的键不存在    KeyError: 'kk' 报错
# print(dict1.pop('k2'))


# popitem   方法删除最后插入字典中的数据。在python解释器3.7 之前的版本中，popitem() 方法删除一个随机项。
# 3.7版本之后 他会删除最后添加到字典的数据
print(dict1.popitem())    # 也是有一个返回值 键和值作为一个元组返回
print(dict1)

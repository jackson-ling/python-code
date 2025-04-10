dict1 = {
    'name':'泽言',
    'age':25,
    '职业':'python讲师'

}
# # """新增/修改键值对"""
# # 如果key不存在进行赋值操作, 那么就会在字典对象里面新增键值对数据
dict1['hobby'] = '打篮球'
print(dict1)
#
# # 如果键存在  则数据会被覆盖(其实就是修改数据)
# dict1['age'] = 26
# print(dict1)

"""字典的合并 update"""
# 合并字典, 如果有不相同的键, 那么会合并《新增一个键值对》; 存在相同的键,那么值会覆盖
dict2 = {'name': '泽言','age': '26','gender': '男', '爱好': '吃喝玩乐'}
dict3 = {'学校': '青灯教育', '爱好': '躺着赚钱'}

dict2.update(dict3)  # 将dict3中的键值对合并到dict2
print(dict2)
print(dict3)
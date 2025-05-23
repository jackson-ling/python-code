"""
{}   表示创建字典对象  英文输入法 变量 = {}

"""
# json类型数据 双引号
# dict1 = {}  # <class 'dict'>
# print(type(dict1))
"""
字典中数据形式是键值对的形式, 即 key: value 的形式
                            键   ----> key(冒号左边是键)
                            不可变的对象做键
                            字典的键必须唯一  键 独一无二的(像我们的身份证一样不能重复)
                            哪些数据类型可以作为字典键?
                            字典的键可以是 字符串/数值/布尔/元组    但是列表/字典/集合是不可以
                            
                             值----->  value 
                             冒号右边是一个值   可以是任意Python类型 
                             
                            

"""


# 简单的字典
# dict2 = {'name':'泽言','age':25}


# 键
# dict3 = {'name':'泽言',4:12,4.2:54,True:58,False:2}
# print(dict3)
# dict4 = {[1,3,4,5]:58}  # 列表不能作为字典键
# print(dict4)
# dict5 = {(5,4,6,7):67}
# print(dict5)
# dict6 = {{'name':123}:66}
# print(dict6)
# dict7 = {{1,4,5}:52}
# print(dict7)

# 字典键的易错点
# 1.字典的键必须唯一(后面的键会把前面的键进行覆盖)
# dict8 = {'age':20,'age':25}  # 在字典里面不要去写名字相同的键
# print(dict8)

# 2.易错点2 数值类型
# # 在数值类型里面字典的哈希值会把8和8.0识别为同一个键 (重点)  整形和浮点型大小相等情况下才会被覆盖
# dict9 = {8:25,8.0:56}
# print(dict9)

# 值  可以是任意Python类型(什么数据类型都OK)
# dict13 = {'name':[1,2,3,4],'name1':{1,3,5},99:{'nn':11}}
# print(dict13)

# 注意点一
# 字典是无序的数据容器(就是说控制台打印的顺序可以和我自己定义的顺序是不一样的,这是正常的,因为字典是无序的数据容器)
# dict7 = {'name': '正心', 'age': 22, 'gender': '男'}
# print(dict7)

# 注意点二
# # # 定义空字典的2种方法
#
# dict71 = {}
# print(type(dict71))
#
dict72 = dict()
print(type(dict72))

# 在后面 字典用的很多 他是可以快速取值的 通过键的唯一性    (后端去对接前端的接口用的是json(双引号)(字典型数据格式(可双可单)



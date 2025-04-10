# # 单引号去创建字符串
# name = '泽言' # <class 'str'> 字符串类型
# print(type(name))
#
#
# # 双引号去创建字符串
# # 在字符串里面单双引号创建字符串没有任何区别是一样的 在你们后面学爬虫的时候(json数据 他只能是双引号)
# name1 = "丸子"
# print(type(name1))
#
#
# # 三引号创建
# name2 = """七月""" # 如果用变量进行了接受 那么此时的三引号就变成的字符串的创建而不是注释
# print(type(name2))
#
# name3 = '''山禾'''
# print(type(name3))

# 单双引号的易错点(不能同种使用，只能混用)
# 在单双引号中只能单引号包裹双引号,或者双引号取包裹单引号 不可以双包双 或者单包单
# # print(''丸子'') # 错误写法
# print('"丸子"')
# print("'丸子'")


# 字符串的拼接    一定要是相同的数据类型
name9 = '泽言'
# age = str(25)
age = '25'
print(type(age))
zhiye = 'python讲师'

print(name9 + zhiye + age) #如果代码出现阴影(代表可能报错,并不是一定)

# 字符串拼接练习
name='jackson'
age='18'
# age1=str(18)
height='163'
print(name+ age+ height)
print(name,age,height,sep=' ')

"""
输入两个数字（input）,相加之后打印输出
"""
# 注意；input返回变量类型默认是字符串，计算要对类型强制转换
# a = input('请输入第一个数字')
# b = input('请输入第二个数字')
# result=(a+b)
# print(result)
# print(type(result))
# 方法一：数据类型强转
# # a = input('请输入第一个数字')
# # b = input('请输入第二个数字')
# # a = int(a)
# # b = int(b)
# # print(a+b)
#
# a = int(input('请输入第一个数字'))
# b = int(input('请输入第二个数字'))
# result=(a+b)
# print(result)
# print(type(result))


# # 方法二；eval剥离最外层的数据类型（str）
a = eval(input('请输入第一个数字'))
b = eval(input('请输入第二个数字'))
result=(a+b)
print(result)
print(type(result))


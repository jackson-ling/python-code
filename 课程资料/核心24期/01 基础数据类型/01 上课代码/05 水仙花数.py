"""
水仙花数是指一个 3 位数，位它的每个上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。

判断 371 是不是水仙花数
"""

# number = 371
# 在我们使用input他返回的是一个str(字符串)的数据类型
number = int(input('请输入你要判断3位数:'))
# python里面的加减乘除等等一切运算都是发生在数值类型之间

# 计算百位  3....71
b = number // 100
print(b)

# 计算十位
s = int(number / 10 % 10)
print(s)
#
# 计算个位 37....1
g = number % 10
# print(g)


# 在我们的python里面=是赋值,==才是比较
# if 可以理解为如果
# 如果if后面的条件是成立的那么他就会执行if下面的语句

if g ** 3 + s ** 3 + b ** 3 == number: # 满足这个条件就说明他是水仙花数
    print(number,'是水仙花数')



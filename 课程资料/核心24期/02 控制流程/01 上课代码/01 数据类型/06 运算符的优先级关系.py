r = 4 > 2 ** 4 or True is 1 and '4' in "345"
# 执行指数的优先级  r = 4 > 16 or True is 1 and '4' in "345"
# 比较运算符       r = False or True is 1 and '4' in "345"
# 身份运算符       r = False or False and '4' in "345"
# 成员运算符       r = False or False and  True (and优先级高于or)
# 逻辑运算符       r = False

#
# print(True is 1)  # 他们引用不是同一个对象
# print(id(True))
# print(id(1))
print(r)

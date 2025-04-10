# 逻辑运算
#     and --> 条件1 and 条件2 两个条件都成立,返回True,否则返回False 和
#     or  --> 条件1 or  条件2 两个条件中的一个条件成立,就返回True   或
#     not --> not 条件, 条件会直接逆转   not(True) ---->False


# and
# print(9 > 4 and 8 < 6)
#
# # or
# print(9 > 4 or 8 < 6)

# and 和 or          and 优先级  大于 or
# print(6 > 5 or 7 < 4 and 7 > 8)

# () 去改变他的优先级
x = (True or False) and False
print(x)

# not(把结果进行逆转)
print(not(9 > 4 and 7 < 5))

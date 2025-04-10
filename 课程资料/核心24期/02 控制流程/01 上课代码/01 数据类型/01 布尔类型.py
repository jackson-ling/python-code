# python 中布尔值使用常量 True 和 False来表示
# true = True
# print(true)
# print(type(true))
# # 布尔类型 <class 'bool'>

# 公式成立是真的 那么就返回布尔结果True
# python他会进行一个底层隐式转换
# print(9 > 7) # 是一个布尔结果


# str 字符串           非空即是True
# print(bool('rrr')) # True
# print(bool(''))  # False
# print(bool(' '))  # True


# 数值类型        非零即使True
print(bool(2)) # True
print(bool(-5)) # True
print(bool(0))  # False

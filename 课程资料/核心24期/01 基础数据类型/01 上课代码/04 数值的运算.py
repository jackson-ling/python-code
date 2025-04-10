one = 1
two = 2
three = 3
four = 4
nine = 9
ten = 10

# 加法 +
print(ten + two)

# 减法 -
print(nine - four)

# * (英文输入法下shift+8)
print(ten * four)

# 英文输入法下/  python里面的除法得出结果是浮点型数据
print(ten / two)

# 取整余 //  9 // 2 4.....1(4才是整余)
print(nine // two)

# 取余数  9 % 2 4.....1(1就是余数)
print(nine % two)

# 幂
print(ten ** 3)  # 表示3个10相乘
# 开方
import math
a = 6
b = 9
c = 6 ** 2 + 9 ** 2
x = math.sqrt(c)
print(format(x, ".2f"))
# 保留小数
a=3.123
print(format(a,'.2f'))    #方法一
print(f'{a:.2f}')   #方法二

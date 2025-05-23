#                             round函数
'''
特殊情况，当小数点为5的时候慧舍入到最近的偶数
例如：
3.5---4
0.5---0
5.5---6
'''
print(round(3.5))
print(round(4.2))
print(round(5.6))

#四舍五入负数（和正数一样，最后把符号加上就行）
print(round(-3.6))  # -4
print(round(-3.4))  # -3

#round函数四舍五入保留小数点位数
print(round(2.125,2))	# 2.12（2就是保留两位小数）


#特殊运用
# 四舍五入到整数（小数点左边的数字）
print(round(123.456, -1))  # 120.0
print(round(126.123, -1))  # 130.0
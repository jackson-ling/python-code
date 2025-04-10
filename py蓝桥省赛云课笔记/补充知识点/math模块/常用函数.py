import math

#常量
print(f'圆周率={math.pi}')
print(f'自然对数的底数e={math.e}')


#幂函数

# 计算x的y次方
a=math.pow(2,2)
print(f'2的平方={a}')

# 计算x的平方根
b=math.sqrt(4)
print(f'4的平方根是{b}')

#对数函数
'''
1.math.log(x,y)  以y为底数，x为真数 

注意：如果不指定真数，底数，默认以e为底数，就是4的情况

2.math.log2(x)   以2为底对数
3.math.log10(x)  以10为底的对数
4.math.log(x)    以e为底的对数

例子
import math

print(math.log(math.e ** 10))		# 10.0
print(math.log(8,2))				# 3.0
print(math.log2(8))					# 3.0
print(math.log10(100))				# 2.0

'''


#三角函数
'''
math.sin(x)
math.cos(x)
math.tan(x)
math.asin(x)
math.acos(x)
math.atan(x)

'''


#舍入函数
'''
math.ceil(x)  向上舍入到最近的整数    3.5->4
math.floor(x)  向下舍入到最近的整数   3.5->3
math.fabs(x)   求绝对值
'''


#其他常用函数
'''
math.gcd(a,b)  计算a，b的  “最大”  公约数
math.factorial(x)  计算x的阶乘
math.fmod(x,y)  计算x/y的余数  ----  x%y
'''

#进制转换
'''
1.二进制：print(bin(225))   # 0b11111111	
2.八进制：print(oct(225))   # 0o377
3.十六进制：print(hex(255))	# 0xff
'''
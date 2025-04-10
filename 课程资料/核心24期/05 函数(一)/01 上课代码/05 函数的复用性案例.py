"""
复利公式：
s 是本金 + 利息
p 本金
i 利率
n 投资年限
s = p * (1 + i) ** n  # 固定公式 记住就好了
余额宝 兴全添利宝 年化 2.5610%
假设本金（principal）10000
1、请问分别存 5年 10年 15年 20年后 本金利息共多少
2、如果利率（interest）变成 6% 分别存 5年 10年 15年 20年后 本金利息共多少
3、如果本金变成 20000，利率不变 分别存 5年 10年 15年 20年后 本金利息共多少
"""

# 公式通过不同的参数反复利用得到不同结果 ,这个就是函数的复用性
def f2(p,i,n):
    s = p * (1 + i) ** n # **表示次方
    return s # 实现函数内外的数据共享

# # 调用函数
# # 本金
# principal = 10000
# # 利率
# interest = 2.5610/100
#
# # 1、请问分别存 5年 10年 15年 20年后 本金利息共多少
# print(f2(principal,interest,5))
# print(f2(principal,interest,10))
# print(f2(principal,interest,15))
# print(f2(principal,interest,20))


# 2、如果利率（interest）变成 6% 分别存 5年 10年 15年 20年后 本金利息共多少
# 本金
# principal = 10000
# # 利率
# interest = 6/100
#
# print(f2(principal,interest,5))
# print(f2(principal,interest,10))
# print(f2(principal,interest,15))
# print(f2(principal,interest,20))


#
# 3、如果本金变成 20000，利率不变 分别存 5年 10年 15年 20年后 本金利息共多少
# 本金
principal = 220000
# 利率
interest = 2.5610/100

print(f2(principal,interest,5))
print(f2(principal,interest,10))
print(f2(principal,interest,15))
print(f2(principal,interest,20))


# def f2(p,i,n):
#     s = p * (1 + i) ** n # **表示次方
#     return s # 实现函数内外的数据共享

# 改进版本，动态变化用input（）函数,使用位置参数，一一对应传递值,这里用一个变量接受传递值
principal=float(input('请输入本金:'))
interest=float(input('请输入利率：'))
n=float(input('请输入投资年限：'))
print(f2(principal,interest,n))
# 使用关键字参数
print(f2(p=220000 ,i=2.5610/100 ,n=5))






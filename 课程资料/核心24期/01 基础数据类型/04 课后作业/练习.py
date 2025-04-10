# 1.数字打印相加
# 易错：input输入默认是字符串类型
# a=int(input())
# b=int(input())
# print(a+b)
# print(type(a+b))

# 2.字符串的格式化
a="python"
b="Java"
c="C"
t1=1989
t2=1991
t3=1969
t4=1973
print(f'{a} s是一门动态解释型语言，起源于{t1}年圣诞节期间')
print(f'{b} 是一门静态编译型语言，起源于{t2}年')
print(f'{c} 是一门静态编译型语言，起源于{t3}年到{t4}年期间')
print()
print('{} s是一门动态解释型语言，起源于{}年圣诞节期间'.format(a,t1))
print('{} 是一门静态编译型语言，起源于{}年'.format(b,t2))
print('{} 是一门静态编译型语言，起源于{}年到{}年期间'.format(c,t3,t4))
print()
print('%s s是一门动态解释型语言，起源于%s年圣诞节期间'%(a,t1))
print('%s 是一门静态编译型语言，起源于%s年'%(b,t2))
print('%s 是一门静态编译型语言，起源于%s年到%s年期间'%(c,t3,t4))
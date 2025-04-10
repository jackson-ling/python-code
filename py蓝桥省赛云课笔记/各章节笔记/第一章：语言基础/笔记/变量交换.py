#python不同于C语言，有更简单的方法
a=1
b=2
a,b=b,a
print(f'a={a},b={b}')

#C语言则引用一个中间变量暂时存储
a=1
b=2
c=a
a=b
b=c
print(f'a={a},b={b}')
def f(x,b,c):
    y = x * b + c
    print('x',x)
    print('b',b)
    print('c',c)
    return y


# print(f(5,b=7,c=9))
# print(f(5,x=7,b=9)) # 因为5作为位置参数已经赋值给了x  x的参数位置已经被占用了 所以后面x=7是会报错的,已经没有他的位置了


#  # 如果在进行位置参数和关键字参数的混用
#
#  位置参数必须写在关键字参数的前面(python底层源码规定好的)
#
# print(f(x=6,5,c=8)) # 错误的
print(f(5,b=6,c=7))   #  正确的
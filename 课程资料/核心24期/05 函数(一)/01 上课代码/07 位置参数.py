# 根据形式参数的位置传递的参数, 叫做位置参数, 一一对应
def f(x,b,c):
    y = x * b + c
    print('x',x)
    print('b',b)
    print('c',c)
    return y
#调用
print(f(5,6,7))  # 按照顺序一一对应传值 叫做位置参数
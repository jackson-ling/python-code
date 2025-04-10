# 所谓递归  本质就是自己调用自己
# 需求:给定一个数字, 求 1 到这个数字中所有数字的和
# 3   3 + 2 + 1
# 5   5 + 4 + 3 + 2 + 1

import sys
sys.setrecursionlimit(3000)  # 设置限制的递归次数
def func1(a):
    # 设置一个递归出口
    if a==1:
        return 1  # # return 遇到他函数终止   并且让func1(1)返回1

    result = a + func1(a-1)      # 函数名 + () 表示调用函数，把括号里的值当作参数再一次执行函数
    return result
    # result = 5 + func1(5 - 1) --->result = 5 + func1(4)   会再去执行result = a + func1(a-1)
    # result = 4 + fun1(4 - 1)
    # result = 5 + 4 + fun1(3)      会再去执行result = a + func1(a-1)  result = 3 + func1(3-1)
    # result = 5 + 4 + 3 + func1(2)   会再去执行result = a + func1(a-1)  result = 2 + func1(2-1)
    # result = 5 + 4 + 3 + 2 + func1(1)  这个结果会趋向于负的无穷大

# 调用函数
 # 递归在没有特殊设置次数的时候 默认只能递归1000次(在python里面每一次递归 会丢失 python底层的一个机制 是为了保护电脑的性能)
print(func1(5))
# print(func1(1000))

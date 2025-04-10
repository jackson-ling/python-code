# 需求:给定一个数字, 求 1 到这个数字中所有数字的积
# 3   3 * 2 * 1
# 5   5 * 4 * 3 * 2 * 1

def func(num):
    if num == 1:  # 设置递归出口，如果没有就会一直递归，趋于负的无穷大
        return 1  # return 函数遇到他就会停止
    result = num * func(num - 1)
    return result # 这里return是为了返回上一次函数值执行的结果 传递给下一次函数使用形成一个闭合
# 调用函数执行逻辑
print(func(5))


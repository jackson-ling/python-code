"""（选做题）
打印一百以内的素数
素数一般指质数。质数是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数
9 1 9  3 3 素数的因数肯定是1到本身之间的数  9   3 3  因数肯定是比本身要小的

9   % 2到8 给每一个数取一遍余   只要其中有一个数据的余数为0 那么就表示这个出出了1和他本身之外
                               还有其他的因数 就说明他不是一个素数




1. 打印0-100的所有数字
2. 判断当数字是否是素数
    如果是素数就打印
    如果不是素数就什么都不做
"""

# """自己在下方编写代码实现功能"""
for i in range(2,12): # 外层循环是选择2到100数
    for j in range(2,i):
        if i % j == 0: # 那么就表示他有其他的因数  就表示他不是一个素数
            break # 终止最近循环
    else:# 打印素数   如果break没有被执行 那么else就会被执行
        print(i)





# qq自带的 ctrl +alt +a













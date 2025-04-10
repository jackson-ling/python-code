# 接收输入的字符
char = input()


def print_triangle(n, c):
    """

    :param n: n表示底边多少个字符
    :param c: c表示用什么字符来画三角形
    :return:
    """

    if n % 2 == 0:
        print("请输入奇数，偶数的底边构不成三角形")
        return

    up = (n + 1) // 2  # 三角形的高
    # 比如题目示例底边是5，那么n就是5，
    # up就是 （5+1）//2 = 3，刚好对应示例输出的三角形的高

    for i in range(1, up + 1):
        # 打印空格和字符
        # 比如第一次循环i = 1
        # up - i = 3-1 = 2
        # 2*i - 1 = 2*1-1 = 1
        # 所有第一次循环就是两个空格后面跟一个字符
        # 后面同理
        print(" " * (up - i) + c * (2 * i - 1))


# 调用函数
print_triangle(n = 5,c = char)

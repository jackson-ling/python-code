# 利用函数, 求两个数的最大值
def get_num(num1, num2): # 在定义函数的时候传递的参数叫做形式参数
                         # 他是没有实际意义的,他只是用于占位
    """
    :param num1: 传递进来的第一个数
    :param num2: 传递进来的第二个数
    :return:    返回值
    """
    if num1 >= num2:
        max_nums = num1  # 最大值
    else:
        max_nums = num2  # 最大值

    print(num1)
    print(num2)
    return max_nums  # 将最大值返回给函数外部

# 调用函数 去执行里面的代码逻辑
# print(get_num(7,4)) # 实际参数,如果函数定义的时候设置了参数 那么函数调用的时候一定要进行传参,数量要一致

# 也可以自己手动去输入值
# input 默认返回的是一个str类型
# num1 = int(input('请输入第一个数字:'))
# num2 = int(input('请输入第二个数字:'))
# print(get_num(num1,num2))




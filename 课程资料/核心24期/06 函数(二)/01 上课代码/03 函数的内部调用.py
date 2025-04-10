def func1():
    print('我是func1的内部')  # 第三步

def func2():
    func1()  # 第二步
    print('我是func2的内部')  # 第四步
    return 111


# 函数要被执行 必须先调用
# 因为没有return 所以返回了none
print(func2())  # 第一步 调用函数

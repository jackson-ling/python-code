# else当try代码块下面的代码没有异常的时候我会被执行

try:
    # print(111)
    print(name)
except Exception as r:
    print(r)


# 可以通过else是否被执行 去反推try下面的有没有错误
else:
    print('我是else，当try代码块下面的代码没有异常的时候我会被执行')
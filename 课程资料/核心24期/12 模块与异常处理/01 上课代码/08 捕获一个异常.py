try:
    print(10/0)
    print(name)
except ZeroDivisionError:# 指定的捕获异常 只能捕捉一个名字错误就停止
    print('有错误')
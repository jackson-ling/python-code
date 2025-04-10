def div(a,b):
    try:
        if b == 0:
            raise Exception('b不能111够等于0') # 这个异常是我自己手动抛出的,而不是系统抛出的
        return a/b
    except Exception as e:
        print(e)# 捕获异常信息


# 调用函数 传递参数
# print(div(9,2))
print(div(5,0))
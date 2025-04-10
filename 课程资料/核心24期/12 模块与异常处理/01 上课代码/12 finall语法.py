# finally, 不管try代码块下面的代码有没有异常, 我都会被执行
try:
    print(name)
except Exception as e:
    print(e)


finally:
    print('我是finally, 不管try代码块下面的代码有没有异常, 我都会被执行')
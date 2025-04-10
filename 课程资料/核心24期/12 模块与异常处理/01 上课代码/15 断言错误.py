def div(a,b):
# assert 后面的布尔结果为False就会触发断言  后面的布尔结果为True就不会触发断言
    print(b != 0)
    assert  b != 0 , 'b不等于0,'# 这个是我们自己定义报错,不是系统自己的报错
    return a/b


# print(div(9,0))
# print(div(7,6))
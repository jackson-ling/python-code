num = 10  # 全局变量

def func():
    #  这个全局变量一定不要随便更改 如果引用数据较多,可能会发生错乱
    global num # 如果要通过局部变量去修改全局变量 那就需要使用global进行全局声明
    num = 20  # 局部变量
    return num # 将函数内部的值返回给函数外部 实现内外的数据共享

result = func()  # 接受函数内部结果数据 返回的就是局部变量num
print('局部',result)
# 局部变量和全局变量是没有任何关系的 他们2个属于不同的对象 实在电脑里面开辟了2个不同的内存空间

print('全局',num)

# 他们2个id是不一样的 就说明 他们引用的2个不通对象 就相当于在电脑里面开辟2块内存空间用于保存数据
print(id(result))
print(id(num))

# def get_num(*args,**kwargs):                  # 位置参数永远在关键字参数前面
#     print('传递进来的位置参数',args)     # 返回元祖类型
#     print('传递进来的关键字参数',kwargs) # 字典类型
#     # 先算元组类型
#     total = 0
#     for i in args: # i只不过是讲我们从args里面遍历出来的每一个数据进行变量赋值而已
#         total += i   # 代码是从上往下运行   前要结束了 才会去运行第二个 所以2个之间是没有任何影响的
#
#     # 字典类型数据相加
#     for i in kwargs.values():
#         total += i
#
#     return total # 通过return返回多个内容需要使用逗号进行分割 并且返回的是元组类型
#
# # 不管是定义和调用 位置参数永远在关键字参数的前面
# # 调用函数
# print(get_num(1,25,5,57,a=6,b=9,c=7,d=6))

# 如果是循环的嵌套  遍历的赋值变量不要去取一样的名字 不然会发生数据覆盖的冲突
for i in range(9):
    for i in range(4):
        print(i)
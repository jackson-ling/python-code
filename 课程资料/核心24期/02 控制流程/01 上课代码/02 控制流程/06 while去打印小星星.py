"""打印直角三角形
*
**
***
****
*****
"""
# i = 1
# while i < 6:  # 控制行数 12345
#     # print(i)
#     print('*'*i)
#     i += 1  # 让i自增能够退出死循环,放在下面不会忽略第一个小星星的打印


# 不能使用字符串的乘法，循环打印直角三角形
# 使用到嵌套原理
# i = 2
# j = 1
# while j <= i: # 1 2
#     # print(j)
#     print('*',end='')
#     j += 1

"""打印直角三角形
*
**
***
****
*****
"""

i = 1
while i < 6:  # 外层循环控制行数12345
    # print('外层循环',i)
    j = 1
    while j <= i:  # 内存循环控制星星的数量
        # print('内存循环',j)
        print('*',end='')
        j += 1 # 为了跳出死循环 每一次运行+1
    print() # end不写默认换行
    i += 1

"""
经过一个红绿灯, 如果是红灯就立马停车, 如果是绿灯就继续前行
"""

# ligth = '红灯'
# = 是赋值 == 才是比较
ligth = input('请输入灯的颜色:')
if ligth == '绿灯': # 满足条件   # if 后面的判断条件布尔值是True就表述满足条件
    print('可以同行')

elif ligth == '红灯':
    print('禁止通行')

elif ligth == '黄灯':
    print('左右瞭望 注意安全')


# 用于捕捉其他一些情况 (坏掉了)
# 为了人程序没有bug 可以去处理所有的结果

# elif可以写无数个 但是 同级else只能写一个
else:
    print('其他情况')


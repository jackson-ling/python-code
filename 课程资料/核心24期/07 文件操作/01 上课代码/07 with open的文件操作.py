# with open 区别与open 2个特点:
# 1.上述文件操作, 打开文件操作完后都需要关闭文件, 比较麻烦 with open 可以自动关闭操作的文件
# 2.有属于自己代码块

# 其他的方法和参数都是和open是一模一样的没有区别
# open 用变量去接受 对象
# with open 使用as(作为)一个对象
with open(file='t9.txt',mode='w',encoding='utf-8') as f:
    f.write('123')




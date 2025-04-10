 # 需求1：把code文件夹所有文件重命名 Python_xxxx
# 需求2： 删除Python_ 重命名：1， 构造条件的数据 2. 书写if

import os
a = int(input('请输入你的需求序号:'))
print(os.getcwd())


# 修改工作目录
os.chdir('code')
print(os.getcwd())


# 得到文件夹里面的所有的文件名字 listdir
file_name = os.listdir() # 括号里面不指定路径 默认就是当前的工作目录
# print(file_name)
for i in file_name:
    print(i)
    if a == 1: # 执行需求1的内容
        new_name = 'Python_' + i

    else: # 执行需求2的内容
        new_name = i[7:] # 从索引为7的位置开始取值 一直取完
    os.rename(i, new_name)








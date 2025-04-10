import os
print('当前默认的工作目录:',os.getcwd())

# 修改工作目录 \n 是不是叫做换行符
os.chdir('ii2\\k2')

# 当前py文件的所有目录操作都是基于这个文件夹下面的
print('当前默认的工作目录:',os.getcwd())

with open(file='k56.txt',mode='w',encoding='utf-8') as f:
    f.write('123')
import os
print(os.getcwd()) # 返回的是一个绝对路径


# 需求 我现在要在当前创建一个kk3.txt的文件,还要写入555
# 利用w不存在则自己创建的性质
with open(file='kk3.txt',mode='w',encoding='utf-8') as  f:
    f.write('555')
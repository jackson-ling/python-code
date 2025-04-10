import os
name = 'code'
# # isfile 判断给出的路径是否是一个文件  返回的是布尔结果
# print(os.path.isfile(name))   # 返回的False
#
# # isdir 判断是否为 文件夹   是一个文件夹  返回的是True
# print(os.path.isdir(name))




# os.path.exists 检查路径（文件、目录）是否存在  返回布尔结果
# 针对文件夹
# print(os.path.exists(name))
# print(os.path.exists('KKK'))


# 文件
# print(os.path.exists('t6.txt')) # 存在的就返回True  不存在就是False
# os.mkdir('aa')   # [WinError 183] 当文件已存在时，无法创建该文件。: 'aa'

# 当文件夹不存在就创建, 存在就不管他(非常好用的,防止报错)
# 避免文件存在重复创建报错

if not os.path.exists('a5'):# if 后面对的条件为True才执行下面代码
    os.mkdir('a5')






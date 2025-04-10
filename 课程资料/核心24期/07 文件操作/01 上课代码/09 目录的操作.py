import os# 模块要先导入后使用
# 创建目录(文件夹)  文件是有后缀的
name = 'kk'
# os.mkdir(name)  # 如果文件夹存在要创建就会报错

# 删除文件夹  只能够去删除空文件夹   # 如果文件夹不存在就会报错
# os.rmdir(name)



# 重命名 文件/文件夹  都是可以使用这个方法的
# 针对一下文件夹
os.rename('ii1','ii2')   # 如果文件不存在就会报错


# 针对一下文件  文件都是有后缀的
# os.rename('feng.jpg','xiaom.png')


# 删除文件  最好加\\防止转义
# os.remove('ii\\tk1.txt')



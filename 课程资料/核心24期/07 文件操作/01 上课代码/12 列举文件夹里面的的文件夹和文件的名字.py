import os

print('当前默认的工作目录:', os.getcwd())

# 列出目录下所有的内容（文件、文件夹） 返回的是一个列表
# print(os.listdir())
a1 = os.listdir('ii2') # 指定路径 修改路径
# print(a1)
# for i in a1:
#     # 如果try下面的代码块发生了异常 就回去运行except的内存
#     try:
#         os.remove('ii2' + '\\' + i)  # 只能用于删除文件
#     except:
#         os.rmdir('ii2' + '\\' + i) # 只能用于删除文件夹  有子文件的文件夹不能删除
#



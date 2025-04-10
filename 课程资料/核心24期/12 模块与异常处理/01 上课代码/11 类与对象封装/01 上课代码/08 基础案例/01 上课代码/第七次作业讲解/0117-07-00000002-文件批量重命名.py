"""
请在当前py文件中编辑代码
将code文件夹中为文件名字后面添加 "-python", 文件尾缀不变
"""

import os
# print(os.getcwd()) # 打印工作目录
# # # 目录切换
flag = 2

os.chdir('code')
# # print(os.getcwd()) # 打印工作目录
# # print(os.listdir())
# print(os.listdir('code'))

for i in os.listdir():
    if flag == 1:

        print(i)
        file_split = os.path.splitext(i)  # 将文件名和尾缀分开
        print(file_split)
        new_file_split = file_split[0] + '-python' + file_split[-1]
        print(new_file_split)
        # 进行重命名
        os.rename(i,new_file_split)


    elif flag == 2:
        file_split = os.path.splitext(i)  # 将文件名和尾缀分开
        new_file_split = file_split[0].replace('-python','') + file_split[-1]
        os.rename(i,new_file_split)




















"""
请在当前py文件中编辑代码
将code文件夹中为文件名字后面添加 "-python", 文件尾缀不变 1 ---> 1-python (字符串的拼接)
"""
import os
# 第一步首先去打印自己的工作目录  去看一下后面的文件操作需不需要去进行路径拼接
print(os.getcwd())

# 设置功能选项
a = int(input('请输入你的选项:'))

# 将工作目录切换到code文件夹里面去
os.chdir('code')
print('当前的工作目录', os.getcwd())

# 去获取到文件夹里面的所有的文件名  os.listdir
for i in os.listdir(): # 括号里面什么路径都不指定 默认就是当前工作目录
    # print(i)
    if a == 1:
        file_split = os.path.splitext(i) # 将文件名和尾缀分开 返回一个元组
        # print(file_split)
        new_file_name = file_split[0]  + '-python' + file_split[-1]
        print(new_file_name)

        # 对文件进行重新的命名
        os.rename(i,new_file_name)
    else:
        file_split = os.path.splitext(i)  # 将文件名和尾缀分开 返回一个元组
        print(file_split)
        new_file_name = file_split[0].replace('-python','') + file_split[-1]
        # 对文件进行重新的命名
        os.rename(i, new_file_name)

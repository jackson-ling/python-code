#  需求: 将模拟文件中的文件复制到另一个文件夹中去, 数据也要写入进去,
#  文件名字后面统一加 : [复制]
import os
print(os.getcwd())

# 遍历模拟文件夹下面所有文件名
for file in os.listdir('模拟'):
    # print(file)
    #  创建一个备份文件夹, 用于存放复制的文件
    if not os.path.exists('备份文件夹'):  # if 后面对的条件为True才执行下面代码
        os.mkdir('备份文件夹')

    # 读取旧文件文件里面的数据
    with open(file='模拟\\' +  file,mode='r',encoding='utf-8') as f:
        old_data = f.read()
        # print(old_data)

    # 装备新的文件名字后面统一加[复制]
    old_file_name = os.path.splitext(file) # 将文件名和后缀切分开 返回的是元组
    print(old_file_name)
    # old_file_name[-1] # 逆序取值 从右往左   如果是正序  old_file_name[1]
    new_file_name = old_file_name[0] + '[复制]' + old_file_name[-1] # 组成新的名字

    # 把数据写入到新的文件里面去
    with open('备份文件夹\\ ' + new_file_name,mode='w',encoding='utf-8') as f:
        f.write(old_data)


# 函数就是自己封装的代码
#解释器的库 是官方自己传递的
# 自己去可以自定义模块(自己根据功能去封装)

# 输入要查找的名字input, if如果在列表里面, 就提示"存在", else否则提示 "不存在"
name_list = ['正心', '丸子', '自游', '巳月', '泽言']

name = input('请输入你要查找的名字：')
if name in name_list:
    print('存在')
else:
    print('不存在')
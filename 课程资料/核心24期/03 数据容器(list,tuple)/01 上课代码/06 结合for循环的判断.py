name_list = ['正心', '丸子', '自游', '巳月', '泽言']

name = input('请输入你要查找的名字:')
for i in name_list:
    # 等于是是赋值 ,等等于才是比较
    if name == i:  # 他会把每一个名字进行一一比较然后在打印
        print('存在')
    else:
        print('不存在')
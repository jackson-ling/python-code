"""
1. 程序启动，显示信息管理系统欢迎界面，并显示功能菜单  print
2. 用户用数字选择不同的功能      if和循环的搭配
3. 根据功能选择，执行不同的功能    if和循环的搭配
4. 需要记录学生的 姓名、语文成绩、数学成绩、英语成绩、总分  数据容器
5. 如果查询到指定的学生信息，用户可以选择 **修改** 或者 **删除** 信息  考察我们的数据容器的增删改查
6. 进入或退出时加载或保存数据    with open

"""

str_info = """**************************************************
欢迎使用【学生信息管理系统】V1.0
请选择你想要进行的操作
1. 新建学生信息
2. 显示全部信息
3. 查询学生信息
4. 修改学生信息
5. 删除学生信息

0. 退出系统
**************************************************"""
# 如果在不知道自己的程序要运行多少次的情况下  要选则while True break进行搭配使用
while True:
    # 1.程序启动，显示信息管理系统欢迎界面，并显示功能菜单
    print(str_info)
    # 2.用户用数字选择不同的功能
    action = input('请输入你要执行的操作:')  # 字符串
    # 3.根据功能选择，执行不同的功能
    if action == '1':
        print('1. 新建学生信息')

    elif action == '2':
        print('2. 显示全部信息')

    elif action == '3':
        print('3. 查询学生信息')

    elif action == '4':
        print('4. 修改学生信息')

    elif action == '5':
        print('5. 删除学生信息')

    elif action == '0':
        print('0. 退出系统')
        break  # 进行死循环的退出

    else:  # 处理所有的非上述情况
        print('请输入正确的选择')







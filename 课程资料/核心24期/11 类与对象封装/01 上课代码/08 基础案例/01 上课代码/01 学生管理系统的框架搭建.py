## 需求

# 1. 程序启动，显示信息管理系统欢迎界面， print() 进行打印
# 2. 用户用数字选择不同的功能     input
# 3. 根据功能选择，执行不同的功能  if elif    else
# 4. 需要记录学生的 **姓名**、**语文成绩**、**数学成绩**、**英语成绩** 、**总分**      将数据保存数据容器里面去
# 5. 如果查询到指定的学生信息，用户可以选择 **修改** 或者 **删除** 信息  执行数据容器当然增删改查命令
# 6. 进入或退出时加载或保存数据  with open 对数据进行读取保存

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
#   如果在不知道自己的程序要运行多少次的情况下   死循环和break搭配使用
while True:
    # 1.程序启动，显示信息管理系统欢迎界面,并显示功能菜单
    print(str_info)
    # 2.用户用数字选择不同的功能
    action = input('请输入你选择功能序号:') # 默认返回的是str
    # 3.根据功能选择，执行不同的功能
    if action == '1':# int
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
        break # 退出死循环

    # 如果遇到其他的情况 统一交给else进行处理
    else:
        print('请输入正确的选项')








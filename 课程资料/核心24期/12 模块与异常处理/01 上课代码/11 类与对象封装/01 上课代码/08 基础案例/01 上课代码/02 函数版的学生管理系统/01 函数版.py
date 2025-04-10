"""
1. 程序启动，显示信息管理系统欢迎界面，并显示功能菜单  print
2. 用户用数字选择不同的功能      if和循环的搭配
3. 根据功能选择，执行不同的功能    if和循环的搭配
4. 需要记录学生的 姓名、语文成绩、数学成绩、英语成绩、总分  数据容器
5. 如果查询到指定的学生信息，用户可以选择 **修改** 或者 **删除** 信息  考察我们的数据容器的增删改查
6. 进入或退出时加载或保存数据    with open

"""
import json


def insert_student():
    """录入学生信息返回"""
    name = input('请重新输入学生的姓名:')
    chinese = input('请重新输入学生的语文成绩: ')
    math = input('请重新输入学生的数学成绩: ')
    english = input('请重新输入学生的英语成绩: ')
    stu = {}
    if name:  # 空字符串的布尔判断结果为False
        stu['name'] = name
    if chinese:
        stu['chinese'] = int(chinese)
    if math:
        stu['math'] = int(math)  # 指定键修改值
    if english:
        stu['english'] = int(english)  # 指定键修改值
    stu['total'] = stu['chinese'] + stu['math'] + stu['english']
    return stu
# 查询  修改  删除 都需要找学生
def seaech_student(stu_name,student_s):
    for stu in student_s:
        if stu_name == stu['name']:#找到了
            return stu


with open('students.json', mode='r', encoding='utf-8') as f:
    student_str = f.read()

# [{}{}{}{}{}]
students = json.loads(student_str)  # 将字符串转化为python对象

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
        stu = insert_student()
        students.append(stu)
        print('##### ----- 添加成功 ----- #####')


    elif action == '2':
        print('2. 显示全部信息')
        print('姓名\t语文\t数学\t英文\t总分')
        for stu in students:
            print(f"{stu['name']}\t{stu['chinese']}\t{stu['math']}\t{stu['english']}\t{stu['total']}")  # \t是一个制表符

    elif action == '3':
        print('3. 查询学生信息')
        # 输入学生的姓名, 用于查找
        search_name = input('请输入你要查询的名字:')
        stu = seaech_student(search_name,students)
        if stu:
              print('姓名\t语文\t数学\t英文\t总分')
              print(f"{stu['name']}\t{stu['chinese']}\t{stu['math']}\t{stu['english']}\t{stu['total']}")  # \t是一个制表符
              print('##### ----- 查询成功 ----- #####')

        else:  # 当循环正常结束的时候 else会被执行
            print('该学生不存在, 请检查名字是否输入正确!')

    elif action == '4':
        print('4. 修改学生信息')
        modify_name = input('请输入你要修改的学生姓名:')
        stu = seaech_student(modify_name,students)
        if stu:
            new_stu = insert_student()
            stu.update(new_stu)

        else:  # 当循环正常结束的时候 else会被执行
            print('该学生不存在, 请检查名字是否输入正确!')

    elif action == '5':
        print('5. 删除学生信息')
        # 输入学生的姓名, 用于查找
        del_name = input('请输入您要查询的学生姓名: ')
        stu = seaech_student(del_name,students)
        if stu:
            students.remove(stu)
            # students.pop(students.index(stu))
            print('##### ----- 删除成功 ----- #####')

        else:
            print('该学生不存在, 请检查名字是否输入正确!')


    elif action == '0':
        print('0. 退出系统')
        with open('students.json', mode='w', encoding='utf-8') as f:
            # 字符串和二进制
            # f.write(str(students))  #不建议使用str强转

            # 列表类型转字符串
            # ensure_ascii=False  不使用默认的编码 让他正常显示中文
            student_str = json.dumps(students, ensure_ascii=False)
            # print(student_str)
            # print(type(student_str))
            f.write(student_str)
        break  # 进行死循环的退出

    else:  # 处理所有的非上述情况
        print('请输入正确的选择')

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
import json


# 封装一个重新赋值的逻辑
def insert_student():
    """信息录入"""
    name = input('请重新输入你的名字:')
    chinese = input('请重新输入你的语文成绩:')
    math = input('请重新输入你的数学成绩:')
    english = input('请重新输入你的英语成绩:')
    stu = {} # 需要对stu进行重新声明他是一个什么东西  因为他现在不是列表里面遍历出来的
    if name:  # 非空即使true   空字符串的布尔判断结果为False 使用自己原来的名字
        stu['name'] = name  # 通过字典键覆盖去达到修改的目的
    if chinese:  # 非空即使true   空字符串的布尔判断结果为False
        stu['chinese'] = int(chinese)  # 通过字典键覆盖去达到修改的目的  如果不执行 stu['chinese'] = int(chinese)
        # 这个 键是不会被创建的 报了没有键的错误
    if math:  # 非空即使true   空字符串的布尔判断结果为False
        stu['math'] = int(math)  # 通过字典键覆盖去达到修改的目的
    if english:  # 非空即使true   空字符串的布尔判断结果为False
        stu['english'] = int(english)  # 通过字典键覆盖去达到修改的目的
        # 总分应该是前面的数据重新覆盖更新之后再去计算
    stu['total'] = stu['chinese'] + stu['math'] + stu['english']
    return stu # stu就是保存着学生信息的字典  return 是实现函数内外数据共享
    # 在后面调用这个函数的时候 我返回的结果就stu这个字典数据
    # 不能够实现敲回车问题 在我们后面的类与对象可以解决这个 了解为什么会发生这个问题就可以了

# 查询  修改  删除 都需要找学生
def search_student(stu_name,student_s): # stu_name是要找的名字,student_s在哪里找范围
    for stu in student_s:
        if stu_name == stu['name']: # 表示找到了
            return stu # stu就是遍历出来的信息所在的整个字典
        # else 不写默认返回空 如果没有知道返回的就是空




# 在整个系统对学生进行增删改查操作的时候需要的是 [{}, {}, {}] 列表
# 当我们进入系统的时候是需要对原来有的数据进行加载的
with open('students.json',mode='r',encoding='utf-8') as f:
    student_s = f.read() #  # 使用read方法读取的是str类型数据

# 因为我是在操作列表的增删改查 但是现在返回的是str  需要将str 变成 列表类型
students = json.loads(student_s) # 将str转化为列表类型     students 里面保存就加载之后的全部信息

#   如果在不知道自己的程序要运行多少次的情况下   死循环和break搭配使用
while True:
    # 1.程序启动，显示信息管理系统欢迎界面,并显示功能菜单
    print(str_info)
    # 2.用户用数字选择不同的功能
    action = input('请输入你选择功能序号:') # 默认返回的是str
    # 3.根据功能选择，执行不同的功能
    if action == '1':# int
        print('1. 新建学生信息')
        stu = insert_student() # 返回的是一个学生的字典数据
        students.append(stu) # 将数据添加列表里面去
        print('##### ----- 添加成功 ----- #####')
    elif action == '2':
        print('2. 显示全部信息')
        print('姓名\t语文\t数学\t语文\t总分')
        for stu in students:
            # print(stu)
            # 只能是但包双 或者双包单 不能是单包单 或者双包双
            print(f"{stu['name']}\t{stu['chinese']}\t\t{stu['math']}\t\t{stu['english']}\t\t{stu['total']}")
            # \t代表制表符
        print('##### ----- 显示成功 ----- #####')
    elif action == '3':
        print('3. 查询学生信息')
        # 输入学生的姓名, 用于查找
        search_name = input('请输入你要查询的名字:')
        stu = search_student(search_name,students)

        if stu: # 利用非空即使True
                print('姓名\t语文\t数学\t语文\t总分')
                print(f"{stu['name']}\t{stu['chinese']}\t\t{stu['math']}\t\t{stu['english']}\t\t{stu['total']}")
                print('##### ----- 查询成功 ----- #####')

        else:  # 当循环正常结束的时候 else会被执行
            print('该学生不存在, 请检查名字是否输入正确!')

    elif action == '4':
        print('4. 修改学生信息')
        # 输入学生的姓名, 用于修改
        modify_name = input('请输入你要修改的名字:')
        stu = search_student(modify_name,students)

        if stu:#如果找到返回的是一个字典 如果没有找到返回的是空字符
            new_stu = insert_student()  # 返回的是一个保持着学生数据的字典
            stu.update(new_stu)    # 利用 相同键覆盖不同键合并的特性我去修改字典
        # 没有找到
        else:
            print('该学生不存在, 请检查名字是否输入正确!')
        # print(students)

    elif action == '5':
        print('5. 删除学生信息')
        # 输入名字去查找删除的对象
        del_name = input('请输入你要删除的名字:')
        stu = search_student(del_name,students)

        if stu:#如果找到返回的是一个字典 如果没有找到返回的是空字符
                # pop(默认是删除最后一个列表数据, 也可以指定索引在列表中删除数据)
                # students.pop(students.index(stu))   # 获得索引 通过索引删除
                # remove(根据数据在列表中删除)
                students.remove(stu)  # 通过删除指定数据 这种方法是最简单的
                # del stu  后面跟的是索引或者列表的名字
                print('##### ----- 删除成功 ----- #####')

        else:
            print('该学生不存在, 请检查名字是否输入正确!')

        # print(students)

    elif action == '0':
        print('0. 退出系统')
        # 当退出系统的时候需要把数据保存到文件里面去
        with open('students.json', mode='w', encoding='utf-8') as f:
            # write只能写入 二进制和str
            # f.write(str(students)) # 这种方法是不行的 # 如果使用str强转 那么保存的不睡json类型的数据 在后的操作和取值是会有问题
            # 这个是因为json在进行序列化时，默认使用的是编码SCAII，而中文为Unicode编码，ASCII中不包含中文，所以出现了乱码。
            # 在我们保存的时候需要把list列表类型转化成str类型
            # ensure_ascii = False 表示不去使用编码SCAII 让中文可以正常显示
            students_str = json.dumps(students, ensure_ascii=False)  # 将列表数据变回str类型
            # print(students_str)
            # print(type(students_str))
            f.write(students_str)
        break # 退出死循环

    # 如果遇到其他的情况 统一交给else进行处理
    else:
        print('请输入正确的选项')








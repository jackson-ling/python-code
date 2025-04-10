## 需求

# 1. 程序启动，显示信息管理系统欢迎界面，并显示功能菜单 print 打印欢迎界面
# 2. 用户用数字选择不同的功能   if  elif  else
# 3. 根据功能选择，执行不同的功能   if  elif  else
# 4. 需要记录学生的 **姓名**、**语文成绩**、**数学成绩**、**英语成绩** 、**总分**   使用的数据容器 字典 列表 集合 元组
# 5. 如果查询到指定的学生信息，用户可以选择 **修改** 或者 **删除** 信息  数据容器的增删改查
# 6. 进入或退出时加载或保存数据   with open r 读取数据
#                               with open w 写入保存原有的内容


import json
# 在我们进入一个系统是的时候 是应该对原来的数据进行加载
# 在整个系统对学生进行增删改查操作的时候需要的是 [{}, {}, {}] 列表
with open('students.json',mode='r',encoding='utf-8') as f:
    students_str = f.read()   # 使用read方法读取的是str类型数据
    # print(students_str)
    # print(type(students_str))
# 我要把他转成列表的数据类型
# students 里面所保存的就是所有的学生信息 [{}{}{}{}{}]
students = json.loads(students_str) # 将str转化为列表类型(python对象)
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
#   如果在不知道自己的程序要运行多少次的情况下    死循环搭配我们break使用
while True:
    # 1.程序启动，显示信息管理系统欢迎界面，并显示功能菜单
    print(str_info)
    # 2.用户用数字选择不同的功能
    action = input('请输入你要操作的功能:') # str
    if action == '1': # int
        print('1. 新建学生信息')
        name = input('请输入你的名字:')
        chinese = int(input('请输入你的语文成绩:'))
        math = int(input('请输入你的数学成绩:'))
        english = int(input('请输入你的英语成绩:'))

        total = chinese + math + english  # 总分成绩
        stu = {'name': name, 'chinese': chinese, 'math': math, 'english': english, 'total': total}
        students.append(stu) # 将新建的学生信息字典添加到列表里面去
        print('##### ----- 添加成功 ----- #####')


    elif action == '2':
        print('2. 显示全部信息')
        print('姓名\t语文\t数学\t英语\t总分')
        for stu in students:
            # print(stu) # stu就是我们遍历出来的每一个字典
            # 只能是但包双 或者双包单 不能是单包单 或者双包双
            print(f"{stu['name']}\t{stu['chinese']}\t\t{stu['math']}\t\t{stu['english']}\t\t{stu['total']}")
        # \t只是为了美观 自己去调整就可以了
        print('##### ----- 显示成功 ----- #####')

    elif action == '3':
        print('3. 查询学生信息')
        # 输入学生的姓名, 用于查找
        search_name = input('请输入你要查询的名字:')
        for stu in students: #这个stu原本就是有数据不是空的 所以不想修改敲回车可以使用原来的数据
            # 如果遍历的学生字典中名字是要查找的学生姓名
            if stu['name'] == search_name:  # 成功找到了
                print('姓名\t语文\t数学\t英语\t总分')
                print(f"{stu['name']}\t{stu['chinese']}\t\t{stu['math']}\t\t{stu['english']}\t\t{stu['total']}")
                print('##### ----- 查询成功 ----- #####')
                break  # 如果执行了break就表示他是非正常跳出循环 else是不会被执行的

        else:  # 当循环正常结束的时候 else会被执行
            print('该学生不存在, 请检查名字是否输入正确!')


    elif action == '4':
        print('4. 修改学生信息')
        # 输入学生的姓名, 用于修改

        modify_name = input('请输入你要修改的名字:')
        for stu in students:
            if stu['name'] == modify_name:  # 表示成功找到了数据 # 现在的stu 是有数据的 如果不想修改用的就是原来的
                # 方法二
                print('不想修改改内容,请敲回车跳过')  # 此时敲的回车就相当于一个空字符
                name = input('请重新输入你的名字:')
                chinese = input('请重新输入你的语文成绩:')
                math = input('请重新输入你的数学成绩:')
                english = input('请重新输入你的英语成绩:')

                if name:  # 非空即使true    # 空字符串的布尔判断结果为False 使用自己原来的名字
                    stu['name'] = name  # 通过字典键覆盖去达到修改的目的
                if chinese:  # 非空即使true    # 空字符串的布尔判断结果为False 使用自己原来的名字
                    stu['chinese'] = int(chinese)  # 通过字典键覆盖去达到修改的目的
                if math:  # 非空即使true    # 空字符串的布尔判断结果为False 使用自己原来的名字
                    stu['math'] = int(math)  # 通过字典键覆盖去达到修改的目的
                if english:  # 非空即使true    # 空字符串的布尔判断结果为False 使用自己原来的名字
                    stu['english'] = int(english)  # 通过字典键覆盖去达到修改的目的
                # 总分应该是前面的数据重新覆盖更新之后再去计算
                stu['total'] = stu['chinese'] + stu['math'] + stu['english']
                print('##### ----- 修改成功 ----- #####')
                break

        # 没有找到
        else:
            print('该学生不存在, 请检查名字是否输入正确!')
        print(students)

    elif action == '5':
        print('5. 删除学生信息')

        # 输入学生姓名用于删除
        del_name = input('请输入你要删除的名字:')
        for stu in students:
            if stu['name'] == del_name:  # 成功找到了
                # pop(默认是删除最后一个列表数据, 也可以指定索引在列表中删除数据)
                # students.pop(students.index(stu))    # 获得索引 通过索引删除
                # remove(根据数据在列表中删除)
                students.remove(stu)  # 这种方法是最简单的
                print('##### ----- 删除成功 ----- #####')
                break  # 找到就退出
        else:
            print('该学生不存在, 请检查名字是否输入正确!')


    elif action == '0':
        print('0. 退出系统')
        # 当退出系统的时候需要把数据保存到文件里面去
        with open('students.json', mode='w', encoding='utf-8') as f:
            # write只能写入 二进制和str
            # f.write(str(students)) # 不建议大家这么做的 因为json后缀的文件要保存json形式的数据
            # 这个是因为json在进行序列化时，默认使用的是编码SCAII，而中文为Unicode编码，ASCII中不包含中文，所以出现了乱码。
            # 在我们保存的时候需要把list列表类型转化成str类型
            # JSON数据但是双引号   这个是他的特点
            students_str = json.dumps(students, ensure_ascii=False)
            # print(students_str)
            # print(type(students_str))
            f.write(students_str)
        break #退出死循环

    # 处理所有的非上述情况 保证代码的严谨性 也就是不出bug
    else:
        print('请输入正确的选项')






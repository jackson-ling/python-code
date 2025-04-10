"""
第一类  针对学生而言   ------->专门用于保存学生的信息的 比如名字 各科成绩

第二类  针对系统而言   ------> 用于代码逻辑的书写 比如 数据的增删改查一系列操作
"""
import json


# [{},{},{},{}], 通过for循环把字典一个一个遍历出来 然后在通过字典的键去取他对应的值
# [对象,对象,对象]    通过for循环把字典一个一个遍历出来  对象.属性名字去去他的值
# 用于保存学生的信息
class Student:
    """学生类"""
    def __init__(self,name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
        self.total = chinese + math + english
# 实例化
student = Student('泽言',100,100,100)
# print(student) # 我们创建每一个实例化对象是不是就保存着一个学生所有信息
# student1 = Student('丸子',100,100,100)  #
# print(student.name)


# 系统类 用来对保存的学生数据进行增删改查
class StudentManger:
    def __init__(self):
        self.student_list = [] # 定义一个列表用于保存学生类创建的一个一个对象

    # 他是用于整个系统对象的代码逻辑执行 执行函数  我们后面的所有操作都会写在run函数里面
    # 开关函数
    def run(self):
        # 进入系统的时候 对原有学生数据进行加载的
        self.load_student()

        while True:
            # 1.程序启动，显示信息管理系统欢迎界面,并显示功能菜单
            # print(str_info)
            self.show_menu()
            # 2.用户用数字选择不同的功能
            action = input('请输入你选择功能序号:')  # 默认返回的是str
            # 3.根据功能选择，执行不同的功能
            if action == '1':  # int
                print('1. 新建学生信息')
                self.add_student()

            elif action == '2':
                print('2. 显示全部信息')
                self.show_student()

            elif action == '3':
                print('3. 查询学生信息')
                self.search_student()

            elif action == '4':
                print('4. 修改学生信息')
                self.modify_name()

            elif action == '5':
                print('5. 删除学生信息')
                self.del_student()

            elif action == '0':
                print('0. 退出系统')
                self.save_student()
                break  # 退出死循环

            # 如果遇到其他的情况 统一交给else进行处理
            else:
                print('请输入正确的选项')


    # 定义用于加载数据的函数
    def load_student(self):
        with open('students.json',mode='r',encoding='utf-8') as f:
            student_str = f.read() # 返回的str类型
            print(student_str)
            print(type(student_str))
        # 因为我们对数据的增删改查是不是针对列表数据的 str肯定是没有这些方法的
        #  json不能序列化一个空的内容
        students = json.loads(student_str)
        print(students)
        print(type(students))

        # [{}{}{}{}{}]  ----> 转变成  [对象,对象,对象]
        # 由于我们现在使用的是类的封装，所以操作的对象形式要变为[对象,对象]
        # stu 是遍历出来的一个一个字典
        self.student_list = [Student(stu['name'],stu['chinese'],stu['math'],stu['english']) for stu in students]
        print(self.student_list)

    # 用于显示欢迎界面的函数
    def show_menu(self):
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
        print(str_info)

    # 封装用于新增学生信息的函数
    def add_student(self):
        name = input('请输入你的名字:')
        chinese = int(input('请输入你的语文成绩:'))
        math = int(input('请输入你的数学成绩:'))
        english = int(input('请输入你的英语成绩:'))

        # total = chinese + math + english  # 总分成绩
        # [{},{},{}]  ----> [对象,对象,对象]
        # 相当于新增一个一个学生的信息 通过Student变成一个一个对象
        student = Student(name,chinese,math,english)
        # 将对象添加到列表里面去   [对象,对象,对象]
        self.student_list.append(student)
        print('##### ----- 添加成功 ----- #####')
        # students = [
        #     {'name': name, 'chinese': chinese, 'math': math, 'english': english, 'total': total, }
        # ]
        # print(students)

    # 用于显示学生信息的函数
    def show_student(self):
        print('姓名\t语文\t数学\t语文\t总分')
        for stu in self.student_list:
            # stu 一个一个对象   对象.属性 进行取值
            # print(stu)
            # 只能是但包双 或者双包单 不能是单包单 或者双包双
            print(f"{stu.name}\t{stu.chinese}\t\t{stu.math}\t\t{stu.english}\t\t{stu.total}")

            # \t代表制表符
    # 定义用于查询的函数
    def search_student(self):
        # 输入学生的姓名, 用于查找
        search_name = input('请输入你要查询的名字:')

        for stu in self.student_list:
            # 如果遍历的学生字典中名字是要查找的学生姓名
            if stu.name == search_name:  # 成功找到了
                print('姓名\t语文\t数学\t语文\t总分')
                print(f"{stu.name}\t{stu.chinese}\t\t{stu.math}\t\t{stu.english}\t\t{stu.total}")
                break  # 如果执行了break就表示他是非正常跳出循环 else是不会被执行的
        else:  # 当循环正常结束的时候 else会被执行
            print('该学生不存在, 请检查名字是否输入正确!')

    # 定义用于修改的函数
    def modify_name(self):
        # 输入学生的姓名, 用于修改

        modify_name = input('请输入你要修改的名字:')
        for stu in self.student_list:
            # 方法二   (如果遇到不想修改的信息 敲回车跳过)
            if stu.name == modify_name:  # 表示成功找到了数据
                print('不想修改改内容,请敲回车跳过')  # 此时敲的回车就相当于一个空字符
                name = input('请重新输入你的名字:')
                chinese = input('请重新输入你的语文成绩:')  # int不能对空字符强转
                math = input('请输重新入你的数学成绩:')
                english = input('请重新输入你的英语成绩:')

                if name:  # 非空即使true   空字符串的布尔判断结果为False 使用自己原来的名字
                    stu.name= name  # 通过字典键覆盖去达到修改的目的
                if chinese:  # 非空即使true   空字符串的布尔判断结果为False
                    stu.chinese = int(chinese)  # 通过字典键覆盖去达到修改的目的
                if math:  # 非空即使true   空字符串的布尔判断结果为False
                    stu.math = int(math)  # 通过字典键覆盖去达到修改的目的
                if english:  # 非空即使true   空字符串的布尔判断结果为False
                    stu.english = int(english)  # 通过字典键覆盖去达到修改的目的
                # 总分应该是前面的数据重新覆盖更新之后再去计算
                stu.total = stu.chinese + stu.math + stu.english
                break
        # 没有找到
        else:
            print('该学生不存在, 请检查名字是否输入正确!')

    # 用于删除的函数
    def del_student(self):
        # 输入名字去查找删除的对象
        del_name = input('请输入你要删除的名字:')
        for stu in self.student_list:
            if stu.name == del_name:  # 表示已经成功找到了
                # pop(默认是删除最后一个列表数据, 也可以指定索引在列表中删除数据)
                # students.pop(students.index(stu))   # 获得索引 通过索引删除
                # remove(根据数据在列表中删除)
                self.student_list.remove(stu)  # 通过删除指定数据 这种方法是最简单的
                # del stu  后面跟的是索引或者列表的名字
                break
        else:
            print('该学生不存在, 请检查名字是否输入正确!')

    # 用与保存数据的函数
    def save_student(self):
        with open('students.json',mode='w',encoding='utf-8') as f:
            # str/二进制类型
            # f.write(str(self.student_list))
            # print(type(self.student_list))
            # [对象,对象,对象]    -------[{},{},{},{}]
            # 是因为 json.dumps 无法将对象进行序列化的 [{},{},{},{}]
            save_student_list = [{'name':stu.name,'chinese':stu.chinese,'math':stu.math,'english':stu.english,'total':stu.total}for stu in self.student_list]
            # f.write(str(save_student_list)) # 不建议直接使用str进行强转 因为保存不是json数据

            # 在json文件里面保存的数据要是json类型  json的数据都要是双引号数据
            # ensure_ascii=False  不使用默认的编码 让他正常显示中文
            # json.dumps   # 列表类型转字符串

            # json是不能实例化一个空的  至少要去写一个[]
            student_str = json.dumps(save_student_list,ensure_ascii=False)
            f.write(student_str)




# 实例化
StudentManger().run()







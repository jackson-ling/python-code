"""
分为二大类别的
第一类  针对于学生来说      -----> 专门用于保存学生的信息的 比如名字 各科成绩

第二类  针对于整个系统      ------> 用于代码逻辑的书写 比如 数据的增删改查一系列操作

"""
import json
# [{},{},{},{} ]   通过for循环遍历出来的一个个字典 在通过字典的键去获取到他的值
# [对象,对象,对象] 通过for循环遍历出来的一个个对象    实例化对象.属性名称去取他的值
# 第一步定义一个学生;类用于保存我们的字段信息
class Student:
    """学生对象"""
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
        self.total = chinese + math + english  # 统计总分

# 实例化
student = Student('泽言',120,140,110)
print(student)
print(student.chinese)


# 定义我们的一个系统类
class StudentManger:
    """系统对象"""
    def __init__(self):
        self.student_list = []  #定义一个列表用于后面一个个对象的保存

    # 他是用于整个系统对象的代码逻辑执行 执行函数  我们后面的所有操作都会写在run函数里面
    # 开关函数
    def run(self):
        # 加载数据
        self.load_student()
        while True:
            # 1.程序启动，显示信息管理系统欢迎界面，并显示功能菜单
            self.show_menu()
            # 2.用户用数字选择不同的功能
            action = input('请输入你要执行的操作:')  # 字符串
            # 3.根据功能选择，执行不同的功能
            if action == '1':
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
                self.modify_student()

            elif action == '5':
                print('5. 删除学生信息')
                self.del_student()

            elif action == '0':
                print('0. 退出系统')
                self.save_student()
                break  # 进行死循环的退出

            else:  # 处理所有的非上述情况
                print('请输入正确的选择')

    # 封装一个打印欢迎界面的函数
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
    # 用于加载数据的函数
    def load_student(self):
        with open('students.json', mode='r', encoding='utf-8') as f:
            student_str = f.read()
            print(student_str)
            print(type(student_str))
        # [{},{},{}]  ----> 转变成  [对象,对象,对象]
        students = json.loads(student_str)  # 将字符串转化为python对象
        # 由于我们现在使用的是类的封装，所以操作的对象形式要变为[对象,对象]
        self.student_list = [Student(stu['name'],stu['chinese'],stu['math'],stu['english'])for stu in students]
        print(self.student_list)

    # 新建学生信息
    def add_student(self):
        name = input('请输入学生的姓名:')
        chinese = int(input('请输入学生的语文成绩: '))
        math = int(input('请输入学生的数学成绩: '))
        english = int(input('请输入学生的英语成绩: '))
        # total = chinese + math + english  这一步我们学生对象里面已经有了
        # print(total)

        student = Student(name,chinese,math,english)
        self.student_list.append(student) #把对象添加到列表里面去
        # [{},{},{},{}]  [对象,对象,对象]
        # students = [
        #     {'name': name, 'chinese': chinese, 'math': math, 'english': english, 'total': total}
        # ]
        # print(students)
        print('##### ----- 添加成功 ----- #####')

    # 用于显示学生信息的函数
    def show_student(self):
        print('姓名\t语文\t数学\t英文\t总分')
        for stu in self.student_list: # stu就是一个个对象
            print(f"{stu.name}\t{stu.chinese}\t\t{stu.math}\t\t{stu.english}\t\t{stu.total}")  # \t是一个制表符

    # 查询学生信息
    def search_student(self):
        # 输入学生的姓名, 用于查找
        search_name = input('请输入你要查询的名字:')
        for stu in self.student_list:
            # 如果遍历的学生对象中名字是要查找的学生姓名
            if stu.name == search_name:  # 满足的条件
                print('姓名\t语文\t数学\t英文\t总分')
                print(f"{stu.name}\t{stu.chinese}\t\t{stu.math}\t\t{stu.english}\t\t{stu.total}")  # \t是一个制表符
                break
        else:  # 当循环正常结束的时候 else会被执行
            print('该学生不存在, 请检查名字是否输入正确!')


    # 修改学生的信息
    def modify_student(self):
        # 输入学生的姓名, 用于查找
        modify_name = input('请输入你要修改的学生姓名:')
        for stu in self.student_list:
            if stu.name == modify_name:
                # 这里我们就可以输入空字符了 就解决了上次函数封装的问题
                print('如果原有的数据不想修改, 直接敲回车!')
                name = input('请重新输入学生的姓名:')
                chinese = input('请重新输入学生的语文成绩: ')
                math = input('请重新输入学生的数学成绩: ')
                english = input('请重新输入学生的英语成绩: ')
                if name:  # 空字符串的布尔判断结果为False
                    stu.name = name
                if chinese:
                    stu.chinese = int(chinese)
                if math:
                    stu.math = int(math)  # 指定键修改值
                if english:
                    stu.english = int(english)  # 指定键修改值
                stu.total = stu.chinese + stu.math + stu.english

                break
        else:  # 当循环正常结束的时候 else会被执行
            print('该学生不存在, 请检查名字是否输入正确!')

    # 删除学生信息的函数
    def del_student(self):
        # 输入学生的姓名, 用于查找
        del_name = input('请输入您要查询的学生姓名: ')
        for stu in self.student_list:
            # 如果遍历的学生对象中名字是要查找的学生姓名
            if stu.name == del_name:
                # pop(默认是删除最后一个列表数据, 也可以指定索引在列表中删除数据)
                # remove(根据数据在列表中删除)
                self.student_list.remove(stu)  # 返回的是stu整个对象
                # students.pop(students.index(stu))
                break
        else:
            print('该学生不存在, 请检查名字是否输入正确!')
    # 用于保存的函数
    def save_student(self):

        with open('students.json',mode='w',encoding='utf-8') as f:
            # 字符串和二进制
            # [对象,对象,对象]  ----> [{},{},{},{}]
            save_student_list = [{'name':stu.name,'chinese':stu.chinese,'math':stu.math,'english':stu.english,'total':stu.total}for stu in self.student_list]

            # 列表类型转字符串
            # ensure_ascii=False  不使用默认的编码 让他正常显示中文
            # self.student_list [对象, 对象, 对象]
            # json是不可以对列表里面嵌套的对象进行序列化的
            student_str = json.dumps(save_student_list,ensure_ascii=False) # 转化str类型
            # print(student_str)
            # print(type(student_str))
            f.write(student_str)

# 开启代码运行的开关
# 实例化执行代码逻辑 调用开关函数
StudentManger().run()
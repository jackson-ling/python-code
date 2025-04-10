"""
数据库(进阶会讲的)
非关系型数据:mongodb redis....
关系型数据库:mysql  server SQL
 以MySQL为例：
    增  Insert
    删  delete
    改  update
    查  select
    因为这些方法是数据库底层写好的我们只是在根据格式在调用而已
    其实就是封装一个个函数，在函数里面去写代码逻辑 Insert就是函数名字  我们调用这些函数就可以七月实现函数的
    代码逻辑 里面传递的参数都是固定(因为里面的代码逻是提前写好的)

"""

import json


class StuDB:
    def __init__(self):
        self.student_list = []  # [{},{},{}] 操作对象已经发生了改变
        # 项目启动时 去加载原有的数据
        self.load()

    # 加载数据
    def load(self):
        """用于加载数据的函数"""
        with open('students.json', mode='r', encoding='utf-8') as f:
            student_str = f.read()  # str
        # 将str类型转变列表的类型 对数据进行增删改查
        self.student_list = json.loads(student_str)

    # 增加数据的方法
    def insert(self, student):  # 在其他地方调用这个函数把要保存的数据传递过来
        self.student_list.append(student)

    # 数据的删除
    def delete(self, student):
        self.student_list.remove(student)

    # 查找
    def search(self, name):
        for stu in self.student_list:
            # self.student_list 从json文件里面读取出来的这个数据
            if stu['name'] == name:  # 找到了
                return stu  # 返回的stu 是数据所在的整个字典

            # 这里的else不写默认返回空

    # 数据的修改
    def change(self,old_stu,student):# 丸子
        """

        :param old_name:  修改的名字
        :param student:   修改的范围 在哪里修改
        :return:
        """
        # old_stu = self.search(old_name) # 返回数据所在的整个字典
        if old_stu: # 非空即使True
            old_stu.update(student) # 如果有相同的键就覆盖,没有则合并

    # 显示所有数据
    def all(self):
        return self.student_list # 返回的就是全部数据

    # 数据的保存
    def save(self):
        with open('students.json',mode='w',encoding='utf-8') as f:
            # 把数据转化str类型
            # ensure_ascii=False  不使用默认的编码 让他正常显示中文
            student_str = json.dumps(self.student_list,ensure_ascii=False)
            # 只能写入字符串和二进制数据
            f.write(student_str)




# 实例化
db = StuDB()
# db.save() # 如果要调用当前类里面的任意一个方法函数，只需要db.函数()就可以调用




class StudentManger:
    # def __init__(self):
    #     self.student_list = [] # 定义一个列表用于保存学生类创建的一个一个对象

    # 他是用于整个系统对象的代码逻辑执行 执行函数  我们后面的所有操作都会写在run函数里面
    # 开关函数
    def run(self):
        # 进入系统的时候 对原有学生数据进行加载的
        # self.load_student()

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
    # def load_student(self):
    #     with open('students.json',mode='r',encoding='utf-8') as f:
    #         student_str = f.read() # 返回的str类型
    #         print(student_str)
    #         print(type(student_str))
    #     # 因为我们对数据的增删改查是不是针对列表数据的 str肯定是没有这些方法的
    #     #  json不能序列化一个空的内容
    #     students = json.loads(student_str)
    #     print(students)
    #     print(type(students))
    #
    #     # [{}{}{}{}{}]  ----> 转变成  [对象,对象,对象]
    #     # 由于我们现在使用的是类的封装，所以操作的对象形式要变为[对象,对象]
    #     # stu 是遍历出来的一个一个字典
    #     self.student_list = [Student(stu['name'],stu['chinese'],stu['math'],stu['english']) for stu in students]
    #     print(self.student_list)

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

        total = chinese + math + english  # 总分成绩
        # [{},{},{}]  ----> [对象,对象,对象]
        # 相当于新增一个一个学生的信息 通过Student变成一个一个对象
        # [{}, {}, {}]
        # student = Student(name,chinese,math,english)
        # 将对象添加到列表里面去   [对象,对象,对象]
        # self.student_list.append(student)
        stu = {'name': name, 'chinese': chinese, 'math': math, 'english': english, 'total': total}
        db.insert(stu)
        print('##### ----- 添加成功 ----- #####')
        # students = [
        #     {'name': name, 'chinese': chinese, 'math': math, 'english': english, 'total': total, }
        # ]
        # print(students)

    # 用于显示学生信息的函数
    def show_student(self):
        print('姓名\t语文\t数学\t语文\t总分')
        for stu in db.all():
            # stu 一个一个对象   对象.属性 进行取值
            # print(stu)
            # 只能是但包双 或者双包单 不能是单包单 或者双包双
            print(f"{stu['name']}\t{stu['chinese']}\t\t{stu['math']}\t\t{stu['english']}\t\t{stu['total']}")

            # \t代表制表符
    # 定义用于查询的函数
    def search_student(self):
        # 输入学生的姓名, 用于查找
        search_name = input('请输入你要查询的名字:')

        for stu in db.all():
            # 如果遍历的学生字典中名字是要查找的学生姓名
            if stu['name'] == search_name:  # 成功找到了
                print('姓名\t语文\t数学\t语文\t总分')
                print(f"{stu['name']}\t{stu['chinese']}\t\t{stu['math']}\t\t{stu['english']}\t\t{stu['total']}")
                break  # 如果执行了break就表示他是非正常跳出循环 else是不会被执行的
        else:  # 当循环正常结束的时候 else会被执行
            print('该学生不存在, 请检查名字是否输入正确!')

    # 定义用于修改的函数
    def modify_name(self):
        # 输入学生的姓名, 用于修改

        modify_name = input('请输入你要修改的名字:')
        for stu in db.all():
            # 方法二   (如果遇到不想修改的信息 敲回车跳过)
            # 我们现在操作对象[{},{},{}]
            if stu['name'] == modify_name:  # 表示成功找到了数据  泽言
                name = input('请重新输入你的名字:')
                chinese = int(input('请重新输入你的语文成绩:'))
                math = int(input('请重新输入你的数学成绩:'))
                english = int(input('请重新输入你的英语成绩:'))
                total = chinese + math + english  # 计算修改之后的总分
                print('跟新之前的名字',stu['name'])

                # 在跟新之前去使用泽言这个名字查到数据然后再去更改
                # old_stu 所在整个字典
                old_stu = db.search(stu['name'])
                # 就是在更新字典
                stu = {'name': name, 'chinese': chinese, 'math': math, 'english': english, 'total': total}
                #修改逻辑
                # 这里传递的是丸子这个名字 但是我们的json文件是不是没有这个名字的 返回是一个空值
                print('跟新之后的名字', stu['name'])
                db.change(old_stu,stu)


                break
        # 没有找到
        else:
            print('该学生不存在, 请检查名字是否输入正确!')

    # 用于删除的函数
    def del_student(self):
        # 输入名字去查找删除的对象
        del_name = input('请输入你要删除的名字:')
        for stu in db.all():
            if stu['name'] == del_name:  # 表示已经成功找到了
                # pop(默认是删除最后一个列表数据, 也可以指定索引在列表中删除数据)
                # students.pop(students.index(stu))   # 获得索引 通过索引删除
                # remove(根据数据在列表中删除)
                db.all().remove(stu)  # 通过删除指定数据 这种方法是最简单的
                # del stu  后面跟的是索引或者列表的名字
                break
        else:
            print('该学生不存在, 请检查名字是否输入正确!')

    # 用与保存数据的函数
    def save_student(self):
        db.save()
        # with open('students.json',mode='w',encoding='utf-8') as f:
        #     # str/二进制类型
        #     # f.write(str(self.student_list))
        #     # print(type(self.student_list))
        #     # [对象,对象,对象]    -------[{},{},{},{}]
        #     # 是因为 json.dumps 无法将对象进行序列化的 [{},{},{},{}]
        #     save_student_list = [{'name':stu.name,'chinese':stu.chinese,'math':stu.math,'english':stu.english,'total':stu.total}for stu in self.student_list]
        #     # f.write(str(save_student_list)) # 不建议直接使用str进行强转 因为保存不是json数据
        #
        #     # 在json文件里面保存的数据要是json类型  json的数据都要是双引号数据
        #     # ensure_ascii=False  不使用默认的编码 让他正常显示中文
        #     # json.dumps   # 列表类型转字符串
        #
        #     # json是不能实例化一个空的  至少要去写一个[]
        #     student_str = json.dumps(save_student_list,ensure_ascii=False)
        #     f.write(student_str)




# 实例化
StudentManger().run()



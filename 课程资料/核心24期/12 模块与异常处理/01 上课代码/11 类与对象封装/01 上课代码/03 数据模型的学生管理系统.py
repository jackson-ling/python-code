"""
数据库(进阶课程会讲的)
非关系型:Redis,MongBD 等等
关系型    MySQL、SQL Server
   以MySQL为例：
    增  Insert
    删  delete
    改  update
    查  select
    因为这些方法是数据库底层写好的我们只是在根据格式在调用而已
    其实就是封装一个个函数，在函数里面去写代码逻辑，而关键字就是函数名，我们调用这些函数就可以
    实现它里面所对应的功能

"""

"""
# 第一类  代码逻辑书写

# 第二类  是通过函数去封装增删改查这么一些方法
"""
import json
class StuDB:
    """数据模型类: 提供系统中所有关于数据的操作方法 加载数据  数据保存  数据的增删改查"""
    def __init__(self):
        self.student_list = []  #  [{},{},{}] 操作对象已经发生了改变
        # 项目启动时 去加载原有的数据
        self.load()
    # 加载数据
    def load(self):
        """用于加载数据的函数"""
        with open(file='students.json',mode='r',encoding='utf-8') as f:
            student_str = f.read() # str
        # 将str类型转变列表的类型 对数据进行增删改查
        self.student_list = json.loads(student_str)

    # 数据增加
    def insert(self,student): # 在其他地方调用这个函数把要保存的数据传递过来
        self.student_list.append(student)

    # 数据的删除
    def delete(self,student):
        self.student_list.remove(student)


    # 查找
    def search(self,name):
        for stu in self.student_list: # 通过名字取查找数据
            if stu['name'] == name: #找到了
                return stu   # 返回数据所在的整个字典    这里的else不写默认返回空



    # 数据的更改
    def change(self,old_name,student):
        """

        :param old_name: 名字
        :param student: 修改的对象,在哪里修改
        :return:
        """
        old_stu = self.search(old_name) # 返回数据所在的整个字典
        if old_stu:# 非空即使True
            old_stu.update(student)  # 如果有相同的键就覆盖,没有则合并


    # 显示所有的数据
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

#实例化
db = StuDB()
# db.save()  # 如果要调用当前类里面的任意一个方法函数，只需要db.函数()就可以调用



class StudentManger:
    # def __init__(self):
    #     self.student_list = []  # 定义一个列表用于保存学生类创建的一个一个对象

    # 他是用于整个系统对象的代码逻辑执行 执行函数  我们后面的所有操作都会写在run函数里面
    # 开关函数
    def run(self):
        # 首先就应该对系统里面有的数据进行读取加载
        # self.load_student()   # 我这个数据每一次程序启动的是后只需要加载一次就ok 写在死循环的外面
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
                self.modify_name()

            elif action == '5':
                print('5. 删除学生信息')
                self.del_student()

            elif action == '0':
                print('0. 退出系统')
                self.save_student()
                break  # 进行死循环的退出

            else:  # 处理所有的非上述情况
                print('请输入正确的选择')

    # 用于加载数据的函数
    # def load_student(self):
    #     # r 读取模式
    #     with open('students.json', mode='r', encoding='utf-8') as f:
    #         student_str = f.read()
    #         print(type(student_str))
    #     # 因为我们对数据的增删改查是不是针对列表数据的 str肯定是没有这些方法的
    #     # 问你现在急需一种方法将str类型变成列表类型
    #     students = json.loads(student_str)
    #     # print(type(students))
    #     # print(students)
    #
    #     # [{}{}{}{}{}]  ----> 转变成  [对象,对象,对象]
    #     # 由于我们现在使用的是类的封装，所以操作的对象形式要变为[对象,对象]
    #     # stu 是遍历出来的一个一个字典
    #     self.student_list = [Student(stu['name'], stu['chinese'], stu['math'], stu['english']) for stu in students]
    #     # print(self.student_list)
    #
    # # 打印欢迎界面的函数
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
        name = input('请输入学生的姓名:')
        chinese = int(input('请输入学生的语文成绩: '))
        math = int(input('请输入学生的数学成绩: '))
        english = int(input('请输入学生的英语成绩: '))
        total = chinese + math + english
        # print(total)
        # [{},{},{}]  ----> [对象,对象,对象]

        # students = [
        #     {'name': name, 'chinese': chinese, 'math': math, 'english': english, 'total': total}
        # ]
        # print(students)
        # 在这个py文件里面没有了Student这个类 那么此时我们操作的对象[{},{},{}]
        # 变成一个一个学生对象
        stu = {'name': name, 'chinese': chinese, 'math': math, 'english': english, 'total': total}
        db.insert(stu) # 将数据保存到列表里面
        # student = Student(name, chinese, math, english)
        # self.student_list.append(student)  # 把对象添加到列表里面去
        # print('##### ----- 添加成功 ----- #####')

    # 用于显示学生的信息
    def show_student(self):
        print('姓名\t语文\t数学\t英文\t总分')
        # [{},{},{}]  ----> [对象,对象,对象]
        for stu in db.all():
            print(f"{stu['name']}\t{stu['chinese']}\t\t{stu['math']}\t\t{stu['english']}\t\t{stu['total']}")  # \t是一个制表符

    # # 查询学生信息
    def search_student(self):
        # 查询学生信息
        # 输入学生的姓名, 用于查找
        search_name = input('请输入你要查询的名字:')
        for stu in db.all():
            # 如果遍历的学生字典中名字是要查找的学生姓名
            if stu['name'] == search_name:  # 满足的条件
                print('姓名\t语文\t数学\t英文\t总分')
                print(f"{stu['name']}\t{stu['chinese']}\t\t{stu['math']}\t\t{stu['english']}\t\t{stu['total']}")  # \t是一个制表符
                break
        else:  # 当循环正常结束的时候 else会被执行
            print('该学生不存在, 请检查名字是否输入正确!')

    # 修改学生信息
    def modify_name(self):
        modify_name = input('请输入你要修改的名字:')
        for stu in db.all():
            if stu['name'] == modify_name:  # 表示成功找到了数据
                # 方法二
                name = input('请重新输入你的名字:')
                chinese = int(input('请重新输入你的语文成绩:'))
                math = int(input('请重新输入你的数学成绩:'))
                english = int(input('请重新输入你的英语成绩:'))
                total = chinese +math + english # 计算修改之后的总分
                # 更新字典的数据
                stu = {'name': name, 'chinese': chinese, 'math': math, 'english': english, 'total': total}
                # 修改数据
                db.change(stu['name'],stu)
                break
        # 没有找到
        else:
            print('该学生不存在, 请检查名字是否输入正确!')

    # 用于删除数据的函数
    def del_student(self):
        # 输入学生的姓名, 用于查找
        del_name = input('请输入您要查询的学生姓名: ')
        for stu in db.all():
            # 如果遍历的学生字典中名字是要查找的学生姓名
            if stu['name'] == del_name:
                # pop(默认是删除最后一个列表数据, 也可以指定索引在列表中删除数据)
                # remove(根据数据在列表中删除)
                db.all().remove(stu)
                # students.pop(students.index(stu))
                break
        else:
            print('该学生不存在, 请检查名字是否输入正确!')

    # 用于保存数据的函数
    def save_student(self):
        db.save()
        # with open('students.json', mode='w', encoding='utf-8') as f:
        #     # 字符串和二进制
        #     # f.write(str(self.student_list))
        #     # [对象,对象,对象]    ------>  [{},{},{},{}]
        #     # 把列表转化成字符串类型
        #     print('变化之前的',self.student_list)
        #     save_student_list = [{'name':stu.name,'chinese':stu.chinese,'math':stu.math,'english':stu.english,'total':stu.total}for stu in self.student_list]
        #     print('变化之后的',save_student_list)
        #     # f.write(str(save_student_list))
        #     # 在json文件里面保存的数据要是json类型  json的数据都要是双引号数据
        #     # 列表类型转字符串
        #     # ensure_ascii=False  不使用默认的编码 让他正常显示中文
        #     student_str = json.dumps(save_student_list,ensure_ascii=False)
        #     f.write(student_str)


# 实例化对象


StudentManger().run()



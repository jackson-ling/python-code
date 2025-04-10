# 师傅类(父类)
class Master:
    def __init__(self,name,age):
        self.secret = '[古法煎饼果子配方]'
        self.name = name
        self.age = age


    # 方法函数
    def make_cake(self):
        return f'运用了{self.secret}去制作煎饼果子'

# 学校类(父类)
class School:
    def __init__(self):
        self.secret = '[青灯饼果子配方]'


    # 方法函数
    def make_cake(self):
        return f'运用了{self.secret}去制作煎饼果子'

# 定义徒弟类(子类)
class Apprentice(Master,School):
    # 自己的属性先注释,不然他是无法去优先继承第一个父类的属性的 实例属性是不会往后面查找的
    # def __init__(self):
    #     self.secret = '[独创的煎饼果子配方]'
    #
    # # 方法函数
    # def make_cake(self):
    #     return f'运用了{self.secret}去制作煎饼果子'


    # 在子类里面去掉其他多个父类的实力属性和方法函数
    # 类对象去调用(类对象就是类的名字)
    # 调用师傅类的
    def master_make_cake(self):
        Master.__init__(self,self.name,self.age) # 类对象调用 是不会默认传递self

        return Master.make_cake(self) # 类对象调用 是不会默认传递self

    # 调用学校的
    def school_make_cake(self):
        School.__init__(self)  # 类对象调用 是不会默认传递self
        return School.make_cake(self) # 返回方法函数


# 对子类进行实例化

# 如果子类里面自己有的 就会去用自己的
# 只有当前子类什么都没有的情况下才会去继承第一个父类同名方法和属性

#
zeyan = Apprentice('泽言',25)
# 打印属性
print(zeyan.secret)

# 打印方法函数
print(zeyan.make_cake())
print(zeyan.master_make_cake())
print(zeyan.school_make_cake())

# 很多发明 都是一些想偷懒发明出来的
# 减少代码的使用 发明继承这种方法




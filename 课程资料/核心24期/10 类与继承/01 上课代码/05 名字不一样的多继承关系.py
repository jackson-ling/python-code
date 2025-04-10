# 师傅类(父类)
class Master:
    def __init__(self):
        self.secret = '[古法煎饼果子配方]'

    # 方法函数
    def make_cake(self):
        return f'运用了{self.secret}去制作煎饼果子'


# 学校类(父类)
class School:
    def __init__(self):
        self.secret1 = '[青灯饼果子配方]'

    # 方法函数
    def make_cake1(self):
        return f'运用了{self.secret}去制作煎饼果子'


# 定义徒弟类(子类)
class Apprentice(Master, School):
    pass


# 对子类进行实例化
# 子类会默认去继承师傅类的方法函数和实例属性


# 当一个子类去继承多个父类的时候 他会优先去继承第一个父类 同名方法函数和实例属性
# 如果第一个父类没有找到和调用同名的实例属性 ,那么他的实力属性是不会往后继续查找的
# 方法函数是会往后面进行查找的
# 属性不查找，方法查找
zeyan = Apprentice()
# 打印属性
# print(zeyan.secret1)

# 打印方法函数
print(zeyan.make_cake1())

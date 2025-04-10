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
        self.secret = '[青灯饼果子配方]'

    # 方法函数
    def make_cake(self):
        return f'运用了{self.secret}去制作煎饼果子'

# 定义徒弟类(子类)
class Apprentice(Master,School):
    def __init__(self):
        self.secret = '[独创的煎饼果子配方]'

    # 方法函数
    # def make_cake(self):
    #     return f'运用了{self.secret}去制作煎饼果子'


# 对子类进行实例化

# 如果子类里面自己有的 就会去用自己的
# 只有当前子类什么都没有的情况下才会去继承第一个父类同名方法和属性


zeyan = Apprentice()
# 打印属性
print(zeyan.secret)

# 打印方法函数
print(zeyan.make_cake())

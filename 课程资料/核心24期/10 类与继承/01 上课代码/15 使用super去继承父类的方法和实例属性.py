# super一般用于单继承
# 多继承 在子类里面去调用其他父类的方法和属性  是应该使用类对象方法去调用
# 师傅类(父类)
class Master:
    def __init__(self,name):
        self.secret = '[古法煎饼果子配方]'
        self.name = name

    # 方法函数
    def make_cake(self):
        return f'运用了{self.secret}去制作煎饼果子'

# 定义徒弟类(子类)
class Apprentice(Master):
    # def __init__(self):
    #     self.secret = '[独创的煎饼果子配方]'
    # 方法函数
    def make_cake(self):
        super().__init__(self.name) # 是继承父类的实例属性  会默认传递self
        # return f'运用了{self.secret}去制作煎饼果子'
        print(super().make_cake())

# 对子类进行实例化
# 子类会默认去继承师傅类的方法函数和实例属性
zeyan = Apprentice('泽言')
# 打印属性
# print(zeyan.secret)

# 打印方法函数
print(zeyan.make_cake())





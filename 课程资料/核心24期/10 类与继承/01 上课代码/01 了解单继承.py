# 在我们python里面 继承是发生在父类 和 子类之间 子类去继承父类的方法和属性


class A(object):  # 当前object是所有类祖宗 默认继承 object   基类
    def __init__(self):
        self.name = '泽言'
        self.age = 25

    # 定义方法函数
    def info_print(self):
        return f'我是{self.name}'

class C(A): # 子类在继承父类 子类C在继承父类A  括号里面的就是父类
    pass # pass 只是一个占位符 表示什么都不做

# 实例化
c = C() # 对子类进行实例化
print(c.name)
print(c.info_print())

"""
类的继承关系中, 子类会将父类的实例属性和方法继承过来
"""

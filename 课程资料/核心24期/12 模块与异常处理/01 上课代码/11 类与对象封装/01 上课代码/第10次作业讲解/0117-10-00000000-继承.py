"""
请用面向对象的继承的方式实现以下类的封装:

    动物类（Animal）：
        属性：name, high, weight  初始化属性
        行为：吃                   方法函数

    老虎类（Tiger）：
        属性：name, high, weight   老虎 继承动物
        行为：吃、老虎的狩猎技能          老虎的狩猎技能 自己做一个单独封装

    狮子类（Lion）：
        属性：name, high, weight     狮子 继承动物

        行为：吃、狮子的狩猎技能     狮子的狩猎技能   自己做一个单独封装

    狮虎兽（Liger）：
        属性：name, high, weight
        行为：吃、既有老虎的狩猎技能、也有狮子的狩猎技能  就是通过多继承关系
        使用类对象去调用多个父类的方法
"""
"""动物类"""
class Animal:
    def __init__(self,name,high,weight):
        self.name = name
        self.high = high
        self.weight = weight

    # 吃的行为
    def eat(self):
        return f'{self.name}正在吃东西'

"""老虎类"""
class Tiger(Animal):
    # 老虎的狩猎技能
    def hunt(self):
        return f'{self.name}发动了老虎的狩猎技能'

"""狮子类"""
class Lion(Animal):
    # 狮子的狩猎技能
    def hunt(self):
        return f'{self.name}发动了狮子的狩猎技能'

"""狮虎兽"""
class Liger(Tiger,Lion):

    """老虎的狩猎技能"""
    def tiger_hunt(self):
        # 如果类对象在调用父类方法的时候 ,父类有传递的参数 那么是需要通过self进行绑定的
        Tiger.__init__(self,self.name,self.high,self.weight)  # self是不会默认被传递的
        return Tiger.hunt(self)  # 调用方法函数

    """狮子的狩猎技能"""
    def lion_hunt(self):
        Lion.__init__(self,self.name,self.high,self.weight)
        return Lion.hunt(self)

# 进行实例化

tiger = Tiger('虎大','50cm','80kg')
print(tiger.name)
print(tiger.hunt())


lion = Lion('辛巴','60cm','90kg')
print(lion.name)
print(lion.hunt())

liger = Liger('狮虎兽','80cm','60kg')
print(liger.tiger_hunt())
print(liger.lion_hunt())
print(liger.eat())























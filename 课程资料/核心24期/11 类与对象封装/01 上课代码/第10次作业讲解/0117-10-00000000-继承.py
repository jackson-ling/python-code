"""
请用面向对象的继承的方式实现以下类的封装:

    动物类（Animal）：
        属性：name, high, weight
        行为：吃  方法函数

    老虎类（Tiger）： 取继承  Animal 只需要取封装老虎的狩猎技能
        属性：name, high, weight
        行为：吃、老虎的狩猎技能

    狮子类（Lion）：    取继承  Animal     只需要取封装狮子的狩猎技能
        属性：name, high, weight
        行为：吃、狮子的狩猎技能

    狮虎兽（Liger）：
        属性：name, high, weight 多继承 子类里面去调用其他父类的方法
        行为：吃、既有老虎的狩猎技能、也有狮子的狩猎技能    类对象去调用多个父类的方法和属性
"""

"""动物类"""
class Animal:
    def __init__(self,name,high,weight):
        self.name = name
        self.high = high
        self.weight = weight

    # 封装吃的方法函数
    def eat(self):
        return f'{self.name}正在吃东西'

"""老虎类"""
class Tiger(Animal): # 老虎 继承动物 此时动物的方法和属性都会被继承
    # 封装老虎的狩猎技能
    def hunt(self):
        return f'{self.name}发动了老虎的狩猎技能'



"""狮子类"""
class Lion(Animal): # 狮子 继承动物 此时动物的方法和属性都会被继承
    # 狮子的狩猎技能
    def hunt(self):
        return f'{self.name}发动了狮子的狩猎技能'


"""狮虎兽"""
class Liger(Lion,Tiger):
    # 使用到类对象去调用其他父类的方法函数
    # 老虎的狩猎技能
    def tiger_hunt(self):
        # 在多继承里面  如果子要去调用多个父类的方法和实例属性,通过类对象(类名)去调用
        Tiger.__init__(self,self.name,self.high,self.weight)   # self是不会默认被传递的
        return Tiger.hunt(self)
        # super().__init__( self.name, self.high, self.weight)
        # return super().hunt()

    # 老虎的狩猎技能
    def lion_hunt(self):
        # 在多继承里面  如果子要去调用多个父类的方法和实例属性,通过类对象(类名)去调用
        Lion.__init__(self, self.name, self.high, self.weight)  # self是不会默认被传递的
        return Lion.hunt(self)
        # super().__init__(self.name, self.high, self.weight)
        # return super().hunt()
        # super()只适用于单继承关系 因为他只会继承第一个父类的属性和方法
# 实例化老虎类
# tiger = Tiger('虎大','40cm','80kg')
# print(tiger.name)
#
# print(tiger.hunt())

# 实例化狮子类
# lion = Lion('辛巴','40cm','80kg')
# print(lion.name)
# print(lion.hunt())



# 狮虎兽进行实例化
liger = Liger('狮虎兽','40cm','70kg')
print(liger.tiger_hunt())
print(liger.lion_hunt())


# 多继承 类对象
# 单继承 super







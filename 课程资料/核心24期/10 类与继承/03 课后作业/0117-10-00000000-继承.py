"""
请用面向对象的继承的方式实现以下类的封装:

    动物类（Animal）：
        属性：name, high, weight
        行为：吃

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

class Animal:

    def __init__(self,name,high,weight):
        self.name = name
        self.high = high
        self.weight = weight

    def eat(self):
        print(f'{self.name}正在吃东西..')


class Tiger(Animal):

    def __init__(self,name,high,weight):
        super().__init__(name,high,weight)

    def eat(self):
        super().eat()

    def hunt(self):
        print(f'tiger-{self.name}正在狩猎..')


class Lion(Animal):

    def __init__(self, name, high, weight):
        super().__init__(name, high, weight)

    def eat(self):
        super().eat()

    def hunt(self):
        print(f'lion-{self.name}正在狩猎..')

class Liger(Tiger,Lion):

    def __init__(self, name, high, weight):
        super().__init__(name, high, weight)

    def eat(self):
        super().eat()

    def tiger_hunt(self):
        Tiger.hunt(self)

    def lion_hunt(self):
        Lion.hunt(self)


liger1 = Liger('lige',180,80)

print(liger1.name)
print(liger1.high)
print(liger1.weight)

liger1.eat()
liger1.lion_hunt()
liger1.tiger_hunt()





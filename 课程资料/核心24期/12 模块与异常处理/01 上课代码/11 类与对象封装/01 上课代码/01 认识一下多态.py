"""
# 继承: 多态一定是发生在子类和父类之间。
# 重写: 那么方法函数名字肯定是一样的


- 定义父类，并提供公共方法
- 定义子类，并重写父类方法
- 传递子类对象给调用者，可以看到不同子类执行效果不同
"""
"""
需求：
    警务人员和警犬一起工作，警犬分2种：追击敌人和追查毒品，携带不同的警犬，执行不同的工作

"""


# class  定义一个父类

class Dog:
    def work(self):
        pass

# 追击敌人的第一个犬种类
class ArmyDog(Dog):
    def work(self):
        print('追击敌人')

# 稽查毒品的犬类
class DrguDog(Dog):
    def work(self):
        print('稽查毒品')


aa = ArmyDog()
bb = DrguDog()
# 定义警务人员
class Person:
    def work_with_dog(self,dog): # 是需要接受不同犬种的
        dog.work()

zeyan = Person()
zeyan.work_with_dog(aa)   # 我传递的犬种实例化对象是一个子类对象
zeyan.work_with_dog(bb)



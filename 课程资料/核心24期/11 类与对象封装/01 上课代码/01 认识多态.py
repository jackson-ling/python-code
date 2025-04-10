# - 定义父类，并提供公共方法
# - 定义子类，并重写父类方法
# - 传递子类对象给调用者，可以看到不同子类执行效果不同(传递不同的参数 得到不同的结果)


# 继承: 多态一定是发生在父类和子类之间的
# 重写: 父类和子类方法方法函数名字是一样的

"""
需求：
    警务人员和警犬一起工作，警犬分2种：追击敌人和追查毒品，携带不同的警犬，执行不同的工作

"""
# 父类
class Dog:
    def work(self):
        pass

# 追击敌人
class ArmDog(Dog):
    def work(self):
        print('追击敌人')

# 稽查毒品
class DrugDog(Dog):
    def work(self):
        print('稽查毒品')

# 实例化
aa = ArmDog() # 追击敌人
bb = DrugDog() # 稽查毒品

# 定义一个警务人员
class Person:
    # dog 接受其实就一个一个实例化对象  只是一个参数而已 名字是可以随便取得
    def with_dog_work(self,dog):
        # print(dog)
        # 为了调用实例化对象里面的方法
        dog.work()  # 通过实例化对象.去调用相对应的方法函数
zeyan = Person()

# - 传递子类对象给调用者，可以看到不同子类执行效果不同(传递不同的参数 得到不同的结果)
zeyan.with_dog_work(aa)
zeyan.with_dog_work(bb)  # 就是把实例化对象当做参数去传递





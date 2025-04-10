"""
创建一个游戏英雄类，

分别有以下属性  初始化函数  __init__  并且进行绑定
    名字（name），武器（weapon），装备（equipment），血量（blood）

每个英雄类都有游戏技能，分别为（行为）
  攻击（attack）,      # 自己封装的方法函数

创建两个英雄
# 创建多个实例化对象

    '黄忠', '弓箭', ['头盔', '靴子'], 100
    '刘备', '剑', ['头盔', '盔甲'], 100
"""

# 创建一个游戏英雄类，
class Hero:  # 类对象其实就是类的名字
    """在类名下定义的变量就叫做类属性"""
    name1 = '泽言'
    age1 = 25
    def __init__(self,name,weapon,equipment,blood):
        self.name = name
        self.weapon = weapon
        self.equipment = equipment
        self.blood = blood

    # 攻击方法
    def attack(self):
        return f'{self.name}发动了攻击'

    # 定义一个类方法
    @classmethod   # 声明他是一个类方法
    def boat(cls):  # cls 代表的是类     self 实例化对象
        return cls.name1 + '正在上课'    # 使用cls 去掉类属性


   # 定义静态方法  用的比较少  做一个了解  # 声明他是一个静态方法
    @staticmethod  # 声明他是一个静态方法 这种方法用的非常少  做一个了解就好了
    def func():  # 括号里面没有self cls
        return '123456'

# 实例化
hero1 = Hero('黄忠', '弓箭', ['头盔', '靴子'], 100)

hero2 = Hero('刘备', '剑', ['头盔', '盔甲'], 100)


# # """调用类属性的方式"""
# 使用实例化对象去调用
print(hero1.name1)
print(hero2.age1)

# 通过类对象去调用
# print(Hero.age1)
# 通过类对象修改类属性, 会修改所有实例化对象的类属性 相当于全局修改
# Hero.name1 = '泽言1号'
# print(hero2.name1)
# print(hero1.name1)



"""调用类方法"""
# 实例化对象去调用
# print(hero1.boat())

# 通过类对象去调用类方法
# print(Hero.boat())





"""调用静态方法"""
# # 实例化对象调用
# print(hero1.func())
#
#
# # #  通过类对象调用静态方法
# print(Hero.func())


# 偏门的调用方法
# 通过类对象取调用方法函数

print(Hero.attack(hero1))   # 类对象不会默认传递self  ,Hero类对象调用方法函数缺少self self其实就是实例化对象的本身

# 实例化对象
# Hero() # 是会默认去传递self
print(Hero('黄忠', '弓箭', ['头盔', '靴子'], 100).attack())










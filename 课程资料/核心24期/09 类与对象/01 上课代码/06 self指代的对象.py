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
class Hero:
    def __init__(self,name,weapon,equipment,blood):
        self.name = name
        self.weapon = weapon
        self.equipment = equipment
        self.blood = blood

    # 攻击方法
    def attack(self):
        return f'{self.name}发动了攻击'

    def res1(self):
        return self    # 这个返回self本身   # 在类中, self指代的就是实例对象本身


# 实例化
hero1 = Hero('黄忠', '弓箭', ['头盔', '靴子'], 100)

hero2 = Hero('刘备', '剑', ['头盔', '盔甲'], 100)


# a1 = hero1.res1()
# print(a1)   #         a1是不是就是self这个对象
# print(id(hero1))
# print(id(a1))   # 2个id是一模一样的,就代表他们2个引用是同一个对象

# 你用哪一个实例化对象去调用方法,那么这个self就那个实例化对象本身
# a2 = hero2.res1()
# print(id(hero2))
# print(id(a2))





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
    # 方法函数
    def attack(self,who,att):
        # who按照位置参数在接受数据
        print(f'{self.name}攻击{who.name}')  # 实例化对象.调用属性
        who.blood -= att # 血量的减少

# 实例化
hero1 = Hero('黄忠', '弓箭', ['头盔', '靴子'], 100)
hero2 = Hero('刘备', '剑', ['头盔', '盔甲'], 100)

# 把hero2实例化对象当做参数传递
hero1.attack(hero2,20)
# print(hero1.name)
print(hero2.blood)






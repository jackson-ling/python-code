"""
创建一个游戏英雄类， class

分别有以下属性  初始化函数  __init__  并且进行绑定
    名字（name），武器（weapon），装备（equipment），血量（blood）

每个英雄类都有游戏技能，分别为（行为）
  攻击（attack）,      # 自己封装的方法函数
  每一次发动攻击   anger  + 2
  当怒气值达到100的  释放大招

#
创建两个英雄
# 创建多个实例化对象

    '黄忠', '弓箭', ['头盔', '靴子'], 100
    '刘备', '剑', ['头盔', '盔甲'], 100
"""

class Hero:
    def __init__(self,name,weapon,equipment,blood,anger):
        self.name = name
        self.weapon = weapon
        self.equipment = equipment
        self.blood = blood
        self.anger = anger
        self.max_ange = 100# 不需要绑定的 相当于全局变量的定义 下面的哪个函数需要使用  就直接使用self就可以了

    # 定义一个释放大招的函数
    def dazhao(self):
        self.anger = 0 # 释放大招之后  清零怒气值
        # print(f'{self.name}释放了大招')
        return f'{self.name}释放了大招'

    # 攻击技能
    def attack(self):
        self.anger += 2 # 每调用一次这个函数 怒气值加2
        if self.anger >= self.max_ange: # 释放大招
            # a#就是函数调用之后的返回值
            a = self.dazhao() # 出发大招的函数  # 在函数里面去调用另外一个函数self.函数名(固定写法)
            print(a)

        return f'{self.name}发动了攻击'

# 实例化
hero1 = Hero('黄忠', '弓箭', ['头盔', '靴子'], 100,95)
hero2 = Hero('刘备', '剑', ['头盔', '盔甲'], 100,95)

# 我现在要把刘备的头盔取出来
print(hero1.equipment[0])

# 调用攻击方法
print(hero1.attack())
print(hero1.anger)

print(hero1.attack())
print(hero1.anger)

print(hero1.attack()) # 你掉用了哪一个函数 他就会打印谁的一个返回值(只能打印一个return的返回值)
print(hero1.anger)





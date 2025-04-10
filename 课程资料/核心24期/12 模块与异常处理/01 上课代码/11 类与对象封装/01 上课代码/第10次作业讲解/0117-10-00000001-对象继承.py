"""
作业1
在Hero的基础上，新增了法师英雄，多了下面内容

法师（Mage） 继承与hero
    增加属性：魔法值（magical 默认0，最大100）   super去给子类添加新的属性

    - 攻击：    方法函数
        调用一次 怒气 `+2`
        调用一次 魔法值 `+5`

    - 放大招    自己定义的一个个方法函数
      魔法值满时自动放大招

    - 第二形态
      当怒气值满时 自动切换第二形态（魔法值最大值修改为50）
"""
class Hero:
    def __init__(self,name,weapon,equipment,power,blood,anger):
        self.name = name
        self.weapon = weapon
        self.equipment = equipment
        self.power = power
        self.blood = blood
        self.anger = anger
        self.max_anger = 100 # 如果我们的anger达到100 就可以释放大招

    def dazhao(self):
        self.anger = 0
        print(f'{self.name}发动了大招')

    def attack(self):
        print(f'{self.name}发动了攻击')
        self.anger += 2 # 每进行一次攻击怒气值加2
        if self.anger == self.max_anger:
            self.dazhao()

class Mage(Hero):
    def __init__(self,name,weapon,equipment,power,blood,anger,magical): # 新增一个属性
        super().__init__(name,weapon,equipment,power,blood,anger) # 继承父类的属性
        self.magical = magical
        self.max_magical = 100

    # 放大招
    def dazhao(self):
        print(f'{self.name}发动了大招')


    # 切换第二形态
    def second(self):
        print(f'{self.name}切换了第二形态')
        self.max_magical = 50 # 魔法值最大改为50
    # 攻击的方法
    def attack(self):
        print(f'{self.name}发动了攻击')
        self.anger += 2  # 每进行一次攻击怒气值加2
        self.magical += 5  # 魔法值加5
        if self.magical == self.max_magical:
            self.dazhao() # 释放大招
        if self.anger >= self.max_anger: # 切换第二形态
            self.second()
            self.anger = 0


#实例化
mage = Mage('小乔', '扇子', ['衣服', '鞋子'], 10, 100, 96, 35)

print(mage.attack())
print('怒气值:',mage.anger)
print('魔法值:',mage.magical)

print(mage.attack())
print('怒气值:',mage.anger)
print('魔法值:',mage.magical)


print(mage.attack())
print('怒气值:',mage.anger)
print('魔法值:',mage.magical)
















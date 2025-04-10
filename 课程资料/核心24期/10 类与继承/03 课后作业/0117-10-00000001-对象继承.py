"""
作业1
在第九次作业Hero(英雄类)的基础上，新增了法师英雄，多了下面内容(考察super用法与多继承)

法师（Mage）
    增加属性：魔法值（magical 默认0，最大100）   super去添加魔法值

    - 攻击：  需要自己去重写
        调用一次 怒气 `+2`
        调用一次 魔法值 `+5`
    - 放大招
      魔法值满时自动放大招

    - 第二形态 自己封装的一个函数
      当怒气值满时 自动切换第二形态（魔法值最大值修改为50）
"""


class Hero:

    def __init__(self, name, weapon, equipment, power, blood, anger):
        # 初始化属性
        self.name = name
        self.weapon = weapon
        self.equipment = equipment
        self.power = power
        self.blood = blood
        self.anger = anger
        self.max_anger = 5

    def attack(self):
        print(f'{self.name}发动了攻击')
        self.anger += 2
        # if self.anger >= self.max_anger:
        #     self.nirvana()
        #     self.anger = 0

    def nirvana(self):
        print(f'{self.name}发动了大招')


class Mage(Hero):

    def __init__(self, name, weapon, equipment, power, blood, anger, magical):
        super().__init__(name, weapon, equipment, power, blood, anger)
        self.magical = magical
        self.max_magical = 100

    def attack(self):
        super().attack()
        if self.anger >= self.max_anger:
            self.change()
        self.magical += 5
        if self.magical >= self.max_magical:
            print(f'{self.name}发动了大招')

    def change(self):
        print(f'{self.name}切换了第二形态')


hero1 = Hero('韩信', '弓箭', ['头盔', '靴子'], 15, 100, 0)
hero2 = Hero('刘备', '剑', ['头盔', '盔甲'], 20, 100, 0)
hero3 = Hero('李白', '长枪', ['盔甲', '马'], 30, 100, 0)

mage1 = Mage('mage111', '长枪', ['盔甲', '马'], 30, 100, 0, 95)

print(mage1.magical)
mage1.attack()
mage1.attack()
mage1.attack()

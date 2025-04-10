"""
作业1
在第九次作业Hero(英雄类)的基础上，新增了法师英雄，多了下面内容(考察super用法与多继承) 法师去继承英雄类

法师（Mage）

    增加属性：魔法值（magical 默认0，最大100）   super去添加魔法值   super去扩展子类的实例属性

    - 攻击：  需要自己去重写
        调用一次 怒气 `+2` += 2
        调用一次 魔法值 `+5` += 5
    - 放大招
      魔法值满时自动放大招

    - 第二形态 自己封装的一个函数
      当怒气值满时 自动切换第二形态（魔法值最大值修改为50）
"""

"""自己在下方编写代码实现功能"""


class Hero:
    def __init__(self, name, weapon, equipment, power, blood, anger):
        self.name = name
        self.weapon = weapon
        self.equipment = equipment
        self.power = power
        self.blood = blood
        self.anger = anger
        self.max_anger = 100  # 如果我们的anger达到100 就可以释放大招

    # 定义用于释放大招的函数
    def nirvana(self):
        self.anger = 0  # 大招释放完毕 怒气值进行清零
        print(f'{self.name}释放了这一次大招')

    # 定义用于攻击的函数
    def attack(self, who):
        print(who.name)
        # self.blood -= self.power # 减少和攻击力对等的血量  我没有设置攻击了谁

        print(f'{self.name}发动了这一次攻击,攻击了{who.name}')
        who.blood -= self.power
        self.anger += 2  # 每一次攻击怒气值加2
        if self.anger >= self.max_anger:  # 那就说明可以释放大招
            self.nirvana()  # 调用释放大招的函数


# 法师类
class Mage(Hero):
    def __init__(self, name, weapon, equipment, power, blood, anger, magical):  # 新增魔法值的属性
        super().__init__(name, weapon, equipment, power, blood, anger, )  # 继承父类的属性
        self.magical = magical  # 绑定魔法值属性
        self.max_magical = 100  # 定义魔法值数据的临界值

    # 定义释放大招的函数
    def nirvana(self):
        print(f'{self.name}释放了大招')

    # 第二形态的函数
    def second(self):
        # 切换之后 怒取值清零 防止卡bug
        self.anger = 0
        print(f'{self.name}切换第二形态')
        self.max_magical = 50 # 重新赋值


    # 定义攻击函数
    def attack(self):
        print(f'{self.name}发动了这一次攻击')
        self.anger += 2  # 每攻击一次怒气值加2
        self.magical += 5  # 每攻击一次魔法值加5
        if self.magical >= self.max_magical:  # 触发了条件可以释放大招的
            self.nirvana()
        if self.anger >= self.max_anger: # 切换第二形态
            self.second()



# 实例化
mage = Mage('小乔', '扇子', ['衣服', '鞋子'], 10, 100, 96, 35)
mage.attack()
print('怒气值:',mage.anger)
print('魔法值:',mage.magical)

mage.attack()
print('怒气值:',mage.anger)
print('魔法值:',mage.magical)

mage.attack()
print('怒气值:',mage.anger)
print('魔法值:',mage.magical)

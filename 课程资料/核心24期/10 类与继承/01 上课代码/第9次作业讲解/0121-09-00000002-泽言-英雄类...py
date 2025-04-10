"""
### 作业1

1、创建一个游戏英雄类, class
+ 分别有以下属性  保存初始化里面的
  名字（name）,武器（weapon）,装备（equipment）, 攻击力（power）,血量（blood）,怒气（anger）
+ 每个英雄类都有游戏技能,分别为（行为）
  攻击（attack）,放大招（nirvana）  方法函数

用游戏英雄类创建三个游戏人物,分别是（属性）：
    - '韩信','弓箭', ['头盔', '靴子'], 15, 100, 0
    - '刘备', '剑', ['头盔', '盔甲'], 20, 100, 0
    - '李白','长枪',['盔甲', '马'], 30, 100, 0



每个人都有游戏技能,分别为（行为）：
- 攻击
  调用一次 怒气 `+2` （修改anger值）
- 放大招
  怒气值满时自动放大招 (自己设置一个临界值,大于等于这个临界值释放大招)  等于100
"""

"""自己在下方编写代码实现功能"""
class Hero:
    def __init__(self,name,weapon,equipment,power,blood,anger):
        self.name = name
        self.weapon = weapon
        self.equipment = equipment
        self.power = power
        self.blood = blood
        self.anger = anger
        self.max_anger = 100  # 如果我们的anger达到100 就可以释放大招

    # 定义用于释放大招的函数
    def nirvana(self):
        self.anger = 0 # 大招释放完毕 怒气值进行清零
        print(f'{self.name}释放了这一次大招')
    # 定义用于攻击的函数
    def attack(self,who):
        print(who.name)
        # self.blood -= self.power # 减少和攻击力对等的血量  我没有设置攻击了谁

        print(f'{self.name}发动了这一次攻击,攻击了{who.name}')
        who.blood -= self.power
        self.anger += 2 # 每一次攻击怒气值加2
        if self.anger >= self.max_anger: # 那就说明可以释放大招
            self.nirvana() # 调用释放大招的函数

# 实例化
hero = Hero('韩信','弓箭', ['头盔', '靴子'], 15, 100, 95)
hero1 = Hero('刘备', '剑', ['头盔', '盔甲'], 20, 100, 0)

a = int(input('请输入你要攻击的次数:'))
for i in range(0,a):
    hero.attack(hero1)
    print(hero.anger)
    print(hero1.blood) # 打印被攻击者 刘备的血量

# hero.attack()
# print(hero.anger)
# print(hero.blood)
#
# hero.attack()
# print(hero.anger)
# print(hero.blood)


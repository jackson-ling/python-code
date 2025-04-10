"""
### 作业1

1、创建一个游戏英雄类,
+ 分别有以下属性
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
  怒气值满时自动放大招 (自己设置一个临界值,大于等于这个临界值释放大招)
"""

"""自己在下方编写代码实现功能"""

class Hero:

    def __init__(self,name,weapon,equipment,power,blood,anger):
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
        if self.anger >= self.max_anger:
            self.nirvana()
            self.anger = 0

    def nirvana(self):
        print(f'{self.name}发动了大招')


hero1 = Hero('韩信','弓箭', ['头盔', '靴子'], 15, 100, 0)
hero2 = Hero('刘备', '剑', ['头盔', '盔甲'], 20, 100, 0)
hero3 = Hero('李白','长枪',['盔甲', '马'], 30, 100, 0)

hero1.attack()
hero1.attack()
hero1.attack()
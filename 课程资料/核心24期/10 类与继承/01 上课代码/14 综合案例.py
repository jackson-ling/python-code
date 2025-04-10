"""
炼体 PracticeBody
    属性：     init
        名字
        血量(blood)
        体力(power)

    行为：     其实就是我们封装的一个个方法函数
        挑水（carry_water）
            挑水消耗2点体力
        砍柴（chop_wood）
            砍柴消耗3点体力

练气 PracticeMagic
    属性：
        name
        血量
        体力                   有的方法和属性 我就通过继承 继承过来 没有的
      + 灵力（magical_power）  通过super()进行灵力的属性添加的
    行为：
        挑水
            挑水消耗0.2点灵力
        砍柴
            砍柴消耗0.3点灵力
      + 御风(fly)
            御风消耗2点灵力
      + 喷火(spurt_fire)
            喷火消耗2点灵力

练神 PracticeDivine
    属性：
        血量
        体力
        灵力
      + 神力(super_power)  可以通super()进行添加的
    行为：
      - 挑水
      - 砍柴
        御风  fly
            御风消耗0.2点神力
        喷火
            喷火消耗0.2点神力
      + 御剑(flying_sword)
            御剑飞行消耗 2 点神力
"""

class PracticeBody:
    """练体期"""
    def __init__(self,name,blood,power):
        self.name = name # 复制一行 ctrl +d
        self.blood = blood
        self.power = power


    # 挑水
    def carry_water(self):
        self.power -= 2 # 每调用一次这个函数 体力值减2

    # 砍柴
    def chop_wood(self):
        self.power -= 3  # 每调用一次这个函数 体力值减3


class PracticeMagic(PracticeBody): # 炼气期去继承练体期
    """炼气期"""
    # super() 去扩展子类的灵力属性
    def __init__(self,name,blood,power,magical_power): # 新增灵力属性
        super().__init__(name,blood,power) # 继承父类的属性
        self.magical_power = magical_power # 将新增灵力属性绑定到我当前子类对象里面去

    # 挑水
    def carry_water(self):
        self.magical_power -= 0.2  # 每调用一次这个函数 灵力值减0.2

    # 砍柴
    def chop_wood(self):
        self.magical_power -= 0.3  # 每调用一次这个函数 灵力值减0.3

    # 御风
    def fly(self):
        self.magical_power -= 2 # # 每调用一次这个函数 灵力值减2


class PracticeDivine(PracticeMagic): # 炼神期去继承炼气期
    def __init__(self, name, blood, power, magical_power,super_power):  # 新增神力属性
        super().__init__(name, blood, power, magical_power) # 继承父类的属性
        self.super_power = super_power # 将新增神力属性绑定到我当前子类对象里面去

    # 挑水
    def carry_water(self):
       return '我现在没有这个属性'

    # 砍柴
    def chop_wood(self):
        return '我现在没有这个属性'

    # 御风
    def fly(self):
        self.super_power -= 0.2  # 每调用一次这个函数 神力值减0.2

    # 喷火
    def spurt_fire(self):
        self.super_power -= 0.2  # 每调用一次这个函数 神力值减0.2


    # 御剑风行
    def flying_sword(self):
        self.super_power -= 2  # 每调用一次这个函数 神力值减2



# 对最后的子类进行实例化
zeyan = PracticeDivine('泽言',10000,100,20,10)


print(zeyan.chop_wood())

print(zeyan.spurt_fire())
print(zeyan.super_power)























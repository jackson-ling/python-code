"""(这个作业需提交到qq邮箱)
需求：
#
   刘备携带不同装备可以增加不同的属性值（使用多态性质书写代码)
   1.毁灭之刃  属性：增加30点攻击力
   2.冰晶守护  属性：增加25点护甲值
   3.邪神面罩  属性：增加25%的物理吸血
   多态:
   发生在类与类之间    继承关系
   子类去重写父类的方法  函数名是一模一样的
   把子类的实例化对象当做参数传递 获取到不同的结果
"""


# 定义父类
class Equip:
    def attribute(self):
        pass


# 毁灭之刃
class Hui(Equip):
    def attribute(self):
        print('刘备装备了毁灭之刃,增加30点攻击力')


# 冰晶守护
class Shou(Equip):
    def attribute(self):
        print('刘备装备了冰晶守护,增加25点护甲值')


# 邪神面罩
class Xie(Equip):
    def attribute(self):
        print('刘备装备了邪神面罩,增加25%物理吸血')
aa = Hui()
bb = Shou()
cc = Xie()

list1 = []
# 定义使用武器的英雄类
class Liubei:
    # args专门用于接受位置参数
    def with_equip(self,*args):# equip接受是后面传递过来的一个一个实例化对象
        # print(type(args))
        for i in args:
            # 如果函数一旦遇到我们的return  会停止整个函数的执行
            list1.append(i.attribute()) # 是将每一次的结果添加到列表里面去
        # 返回最终的列表数据
        return list1
        # equip.attribute()
        # eq1.attribute()
        # eq2.attribute()

# 实例化英雄类
liubei = Liubei()
liubei.with_equip(bb,cc,aa)





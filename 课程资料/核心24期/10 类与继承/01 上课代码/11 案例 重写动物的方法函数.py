"""养了一只宠物狮子(辛巴)"""


class Lion:
    def __init__(self,name,high,weight):
        self.name = name
        self.high = high
        self.weight = weight

    # 定义方法函数
    def eat(self):
        return f'{self.name}正在吃东西'+'发出卡卡的声音'


class Cat(Lion):
    # pass
    # 用于在不改变父类的属性结构上 在子类里面去添加属于自己的属性
    def __init__(self, name, high, weight,color): # 新增颜色属性
        # 做一个了解 知道有这个方法就可以了 后面仔细的讲解
        # super() 可以调用父类的属性 ,适用于后面的扩展
        # 不改变父类的情况下 去扩展子类自己的属性
        # 通过super绑定我们的属性,绑定到当前对象里面去
        super().__init__(name,high,weight) # 将父类的3个属性继承过来
        self.color = color # 新增的属性也是需要绑定到子类对象里面去的 它是子类所独有的属性,父类里面是没有的
    # 同名的 实例属性是不会往后面查找的 但是方法函数是可以的
    # 全部重写 使用子类的自己的 不去用其他父类的
    # 方法函数 子类里面有的就会去用自己的方法
    def eat(self):
        # 第一步  重写分类的eat方法 名字必须一样
        # 第二步 super()去继承父类的eat方法函数
        # 第三步 改写eat方法
        return super().eat() + '发出卡卡的声音'
# 实例化
# 子类去继承父类的方法和属性
cat = Cat('辛巴','30cm','90kg','棕色')  # 需要传递4个参数
print(cat.name)
print(cat.eat())
print(cat.color)
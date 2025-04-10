"""养了一只宠物狮子(辛巴)"""


class Lion:
    def __init__(self,name,high,weight):
        self.name = name
        self.high = high
        self.weight = weight

    # 定义方法函数
    def eat(self):
        return f'{self.name}正在吃东西'

class Cat(Lion):
    # pass
    def __init__(self, name, high, weight):
        # 做一个了解 知道有这个方法就可以了 后面仔细的讲解
        # super() 可以调用父类的属性 ,适用于后面的扩展
        # 不改变父类的情况下 去扩展子类自己的属性
        # 通过super绑定我们的属性,绑定到当前对象里面去
        super().__init__(name,high,weight)

# 实例化
# 子类去继承父类的方法和属性
cat = Cat('辛巴','30cm','90kg')
print(cat.name)
print(cat.eat())
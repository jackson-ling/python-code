# 动物类
class Animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color

# 狮子类
class Lion:
    def __init__(self,name,high,weight):
        self.name = name
        self.high = high
        self.weight = weight

    # 定义方法函数
    def eat(self):
        return f'{self.name}正在吃东西'


class Cat(Lion,Animal): # 优先继承第一个父类 传递参数数量和第一个父类保持一致
    pass


# 实例化
# 动物类在前
# cat = Cat('辛巴','red')

# print(cat.name)
# print(cat.color)
#
# print(cat.eat())


# 狮子类在前
cat = Cat('辛巴','30cm','60kg')
print(cat.weight)

print(cat.name)

print(cat.eat())
# 属性是不会玩后面去进行查找的
# print(cat.color)

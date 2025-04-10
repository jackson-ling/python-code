# - **私有属性** 就是 **实例对象** 不希望公开的 **属性**
class Woman:
    def __init__(self,name,weight,high,age):
        self.name = name
        self.__weight = weight   # 如果__就带已经变成了私有属性
        self.high = high
        self.age = age

    # 按照正常情况 那肯定是无法修改我的内部代码的

    # 代码是我自己写的 保护起来的

    # 方法函数
    def __print_info(self): # 代表这他已经变成了私有方法
        return f'相亲对象的名字是{self.name}'
    # 间接访问
    def get_weight(self):
        return self.__weight

    def get_1(self):
        return  self.__print_info()# 在函数里面去调用另外一个函数  self



#进行实例化
won = Woman('小红','70kg',165,26)
print(won.name) # 名字是可以成功获取
# print(won.weight)  # 一旦设置了私有 那么外部就无法直接去方法他的私有属性 这个时候就应该内部攻破 间接去访问

print(won.get_weight())
# print(won.print_info())
print(won.get_1()) # 间接的到私有方法的数据
# 他的作用

# 如果你的数据不想被外部访问 这个时候就可以去使用私有属性和私有方法
# 没有绝对安全的
# 直接暴力破解的方法(你需要期知道我写的项目里面的具体变量 具体数据位置,才可以去使用)
# 有锁的钥匙  但是你不知道具体是那一把锁 不知道锁的一个具体位置  看到和获取下来是两码事
# 爬虫 看到数据 爬取下来保存 是不是两回事  用到的时候 才会知道他的具体作用
# 暴力方法只是去获取数据的手段而已 前提是需要自己具体数据的位置保存的方法
# 访问一个属性

# 增加权限  爬虫的  js参数加密  增加你获取数据的难度
print(won._Woman__weight)
# 访问方法函数
print(won._Woman__print_info())



















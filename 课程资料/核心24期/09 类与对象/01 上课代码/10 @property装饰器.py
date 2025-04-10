# 作用: 可以将这个方法通过属性的形式调用, 仅限于类中的函数没有参数的时候才可以这样用
"""泽言养了一只猫"""

class Cat:
    def __init__(self,name,behavior):

        self.name = name
        self.behavior = behavior
    # 方法函数
    @property
    def print_info(self):    # 作用: 可以将这个方法通过属性的形式调用, 仅限于类中的函数没有参数的时候才可以这样用
        return f'{self.name}正在吃东西'

# 对类进行实例化
#  如果 __init__ 中没有参数, 那么实例化对象的时候就不能传参

cat = Cat('加菲猫1号','吃披萨')  # cat只不过是一个别名而已   参数的数量一定要对应不可多也不可少
# # 打印实例属性
print(cat.name)  # 不需要带()

# 获取到他的一个方法  带一个()
print(cat.print_info)



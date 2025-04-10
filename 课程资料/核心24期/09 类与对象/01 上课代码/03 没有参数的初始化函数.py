"""泽言养了一只猫"""

class Cat:
    def __init__(self):
        # 我这个实例属性 是定死的 没有任何的灵活性
        self.name = '加菲猫'
        self.behavior = '猫抓老鼠'

    # 方法函数
    def print_info(self):
        return f'{self.name}正在吃东西'



# 对类进行实例化
#  如果 __init__ 中没有参数, 那么实例化对象的时候就不能传参

cat = Cat()  # cat只不过是一个别名而已
# # 打印实例属性
# print(cat.name)
# print(Cat().name)


# 调用方法函数
print(cat.print_info())
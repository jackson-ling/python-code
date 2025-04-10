"""
### 作业2

1、创建一个房子类, class  类的名字首字母最好大写
+ 分别有以下属性   #   一些需要用到 传递过来的属性 帮初始化函数里面去的
  名字（name）, 房子面积(area), 家具<列表>（furniture）

+ 每个房子都有添加家具的方法 def 封装的方法函数
    # 如果 家具占地面积 <= 房子剩余面积：可以搬入(家具列表添加家具名字数据并房子剩余面积更新：
    # 房屋剩余面积 - 该家具的占地面积 = 目前房子的面积
    # 否则：提示用户家具太大，剩余面积不足，无法容纳  # 房子面积 小于搬进来的家具

2、实例化房子操作
    实例化一个房子， 面积50平米
    添加家具：（沙发，占地15平米）
    添加家具：（餐桌，占地8平米）
    添加家具：（大床，占地20平米）
    添加家具：（浴缸，占地8平米）

"""
"""请在下方编辑代码"""


class House:
    # 将属性绑定我们的初始化函数里面
    def __init__(self,name,area):
        self.name = name # 房子的名字
        self.area = area # 房子的面积
        # 定义空的列表 后面的方法函数需要用的就可以通过self进行调用
        self.furniture = [] # 不需要是绑定  他只是为了方便变量的使用而已

    # 定义添加家具的方法
    def add_jiaju(self,item):
        # print(item)
        if item[1] <= self.area: # 如果搬进来的家具面积小于房子的剩余面积 可以加入
            print(f'{item[0]}添加成功')
            self.furniture.append(item[0]) # 将家具添加到家具列表里面去
            self.area -= item[1]  # 当家具搬进来之后  更新房子的剩余面积
        # 房子剩余面积 小于 家具的面积(无法再添加了))
        else:
            print('提示用户家具太大，剩余面积不足，无法容纳')

# 对类进行实例化
house = House('泽言之家',50)

# 使用实例化对象去调用方法函数 实现里面的代码逻辑
house.add_jiaju(['沙发',15])
print(house.area)
print(house.furniture)

house.add_jiaju(['大床',20])
print(house.area)
print(house.furniture)

house.add_jiaju(['浴缸',16])
print(house.area)
print(house.furniture)

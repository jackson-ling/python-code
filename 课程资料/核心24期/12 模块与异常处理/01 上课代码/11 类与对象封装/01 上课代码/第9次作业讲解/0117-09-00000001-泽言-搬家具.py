"""
### 作业2

1、创建一个房子类,  class 类
+ 分别有以下属性    init
  名字（name）, 房子面积(area), 家具<列表>（furniture）

+ 每个房子都有添加家具的方法   定义的一个 方法函数
    # 如果 家具占地面积 <= 房子剩余面积：可以搬入(家具列表添加家具名字数据并房子剩余面积更新：
    # 房屋剩余面积 - 该家具的占地面积 = 目前房子的面积
    # 否则：提示用户家具太大，剩余面积不足，无法容纳

2、实例化房子操作   他是实例化我们的类
    实例化一个房子， 面积50平米
    添加家具：（沙发，占地15平米）
    添加家具：（餐桌，占地8平米）
    添加家具：（大床，占地20平米）
    添加家具：（浴缸，占地8平米）

"""
"""请在下方编辑代码"""

class House:
    def __init__(self,name,area):  # 除了可以绑定属性,
        self.name = name  # 房子的名字
        self.area = area # 房子他的一个总面积
        self.furniture = []

    def add_juiaju(self,item):
        # print(item)
        if item[1] <= self.area:
            self.furniture.append(item[0])  # 添加家具
            self.area -= item[1]    # 针对每一次家具的面积减少总面积
        else:
            print('家具太大剩余空间不足,无法添加')


# 实例化
house = House('家',50)
house.add_juiaju(['沙发',15])
print(house.area)
print(house.furniture)

# house = House('家',50)
house.add_juiaju(['大床',20])
print(house.area)
print(house.furniture)


house.add_juiaju(['浴缸',25])
print(house.area)
print(house.furniture)









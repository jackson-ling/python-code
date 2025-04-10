"""
### 作业2

1、创建一个房子类, class
+ 分别有以下属性
  名字（name）, 房子面积(area), 家具<列表>（furniture）

+ 每个房子都有添加家具的方法
    # 如果 家具占地面积 <= 房子剩余面积：可以搬入(家具列表添加家具名字数据并房子剩余面积更新：
    # 房屋剩余面积 - 该家具的占地面积 = 目前房子的面积
    # 否则：提示用户家具太大，剩余面积不足，无法容纳

2、实例化房子操作
    实例化一个房子， 面积50平米
    添加家具：（沙发，占地15平米）
    添加家具：（餐桌，占地8平米）
    添加家具：（大床，占地20平米）
    添加家具：（浴缸，占地8平米）

"""
"""请在下方编辑代码"""

class House:

    def __init__(self,name,area,furniture):
        # 初始化属性
        self.name = name
        self.area = area
        self.furniture = furniture
        self.surplus_area = area # 一开始的剩余面积初始化为房子的总面积

    # 添加家具
    def add_furniture(self,target,t_area):
        if t_area <= self.surplus_area: # 如果 家具占地面积 <= 房子剩余面积：可以搬入
            self.furniture.append(target)
            self.surplus_area -= t_area # 剩余面积更新
            print(f'添加家具<{target}>成功！！')
        else: # 否则：提示用户家具太大，剩余面积不足，无法容纳
            print('家具太大，剩余面积不足，无法容纳!!')



house1 = House('white_house',50,[])

house1.add_furniture('沙发',15)
house1.add_furniture('餐桌',8)
house1.add_furniture('大床',20)
house1.add_furniture('浴缸',8)





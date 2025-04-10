"""
模块可以分为3种
         1.内置模块: python解释器自带 不需要通过命令进行下载的  os random   json pprint,time.......
         2.第三方模块: 需要通过命令去cmd进行下载的 pip install  模块名 requests bs4 爬虫数据分析等等第三方模块
         用的最多的,   30w   ,python语言 他就是依赖大量的第三方库实现不同的功能(办公自动化 爬虫 数学分析 机械学习...)
         3.自定义模块: 就是我们自己更具功能去编写的模块 也就是一个一个py文件(自创的)
"""


# 无论是什么模块 都要先导入后使用
# 需求：math模块<内置模块>下 sqrt() 开平方计算

# import 模块名
# 方法一  import 模块名  模块名.功能;
import math
print(math.sqrt(9)) # # 返回的数据是一个浮点型数据

# 方法二 from 模块名 import 功能名   一个模块里面是有很多功能的(模块是保存很多功能的一个盒子)
from math import sqrt
print(sqrt(9))

# 方法三  from 模块名 import *     * 代表当前模块里面的所有功能
from math import *
print(sqrt(9))
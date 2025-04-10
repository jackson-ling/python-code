# -*- coding: utf-8 -*-
"""
作业1：
有N个人要参加会议，现在需要随机安排座位。
请用python实现将N个人随机安排座位

提示： pop 和random.randint结合
    可以导入随机函数模块 random
    random.randint(a, b)
    Return random integer in range [a, b], including both end points.
    在 [a, b] 之间返回一个随机整数，包括 a, b 本身。
"""

import random

name = """
邓永明    廖德超    张勇 杨久林    戴贵富    秦代坤    李元东 田显余
"""
# 有多少个人


site_list = ['1号办公室1位置', '1号办公室2位置', '1号办公室3位置',
             '2号办公室1位置', '2号办公室2位置', '2号办公室3位置',
             '3号办公室1位置', '3号办公室2位置']

# 答案放这里
seating = []
# 答案以二维列表输出 [('1号办公室1位置', '秦代坤'), ('1号办公室2位置', '廖德超'),.......]
"""自己在下方编写代码实现功能"""


# split()将字符串变成列表
name_list = name.split() # 默认以空白字符分割
# print(name_list)
# 1 通过座位随机 就可以人的随机
for i in range(8): # 01234567 控制循环次数
    site_index = random.randint(0,len(site_list)-1)     # 通过索引取人名 左边右边都是闭区间8可以取到的
    # 每一次数据都是从列表里面删除 不会被重复使用
    site_data = site_list.pop(site_index) # 通过pop删除方法有返回值的特性去拿到随机值
    print(site_data)
    print(site_list)
#     # 将数据添加到列表里面去
#     seating.append((site_data,name_list[i]))
# print(seating)
# 2 通过人的随机去实现座位的随机
# for i in range(8): # 01234567 控制循环次数
#     name_index = random.randint(0,len(name_list)-1) # 这里的len是为了实时去检测列表的长度,防止超出索引报错
#     name_data = name_list.pop(name_index) # 通过pop删除方法有返回值的特性去拿到随机值
#
#     seating.append((site_list[i],name_data))
#
# print(seating)

# 3 人和座位都随机

# for i in range(8): # 01234567 控制循环次数
#     # 座位的随机
#     site_index = random.randint(0,len(site_list)-1)     # 通过索引取人名 左边右边都是闭区间8可以取到的
#     site_data = site_list.pop(site_index) # 通过pop删除方法有返回值的特性去拿到随机值
#
#     # 人的随机
#
#     name_index = random.randint(0,len(name_list)-1) # 这里的len是为了实时去检测列表的长度,防止超出索引报错
#     name_data = name_list.pop(name_index) # 通过pop删除方法有返回值的特性去拿到随机值
#
#     # 添加数据
#     seating.append((site_data,name_data))
# print(seating)













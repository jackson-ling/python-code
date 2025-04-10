import json
# [{},{},{},{} ]   通过for循环遍历出来的一个个字典 在通过字典的键去获取到他的值
# [对象,对象,对象] 通过for循环遍历出来的一个个对象    实例化对象.属性名称去取他的值
# 第一步定义一个学生;类用于保存我们的字段信息
class Student:
    """学生对象"""
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
        self.total = chinese + math + english  # 统计总分
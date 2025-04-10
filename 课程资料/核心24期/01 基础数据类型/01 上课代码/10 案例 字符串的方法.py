info_str = """龙猫

主演：秦岚,糸井重里,岛本须美

上映时间：2018-12-14"""


"""
需求：
    1. 拿到主演的姓名（列表）   split()
    2. 将主演名字合并为字符串，中间用中文的逗号隔开  join方法
"""

result = info_str.split() #\n他会被当做空白字符
# print(result)
# # 列表取值(索引)
# print(result[1])
# name = result[1].strip('主演：')
name = result[1].replace('主演：','')
print(name)

# 进行切割 得到列表
name1 = name.split(',')
print(name1)

# 使用join合并成新的字符串
name2 = "，".join(name1)
print(name2)


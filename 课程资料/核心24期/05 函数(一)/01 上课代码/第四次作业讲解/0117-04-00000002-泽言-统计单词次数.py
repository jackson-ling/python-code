# -*- coding: utf-8 -*-
"""
作业4：
统计Python之禅中所有**单词**(注意是单词)出现的次数
"""
# python 之禅
s = """
The Zen of Python, by Tim Peters
Beautiful is better than ugly
Explicit is better than implicit
Simple is better than complex
Complex is better than complicated
Flat is better than nested
Sparse is better than dense
Readability counts
Special cases aren't special enough to break the rules
Although practicality beats purity
Errors should never pass silently
Unless explicitly silenced
In the face of ambiguity, refuse the temptation to guess
There should be one-- and preferably only one --obvious way to do it
Although that way may not be obvious at first unless you're Dutch
Now is better than never
Although never is often better than *right* now
If the implementation is hard to explain, it's a bad idea
If the implementation is easy to explain, it may be a good idea
Namespaces are one honking great idea -- let's do more of those
"""

"""自己在下方编写代码实现功能"""
# 第一步将特殊的一些符号进行去除
result = s.replace('-', '').replace(',', '').replace('*', '')
# print(result)

# 第二步就需要使用字符串的split(分割方法)将单词变成列表里面的一个个元素
result1 = result.split()  # 默认用空白字符分割
# print(result1)

# 第三步去统计每一个单词出现的次数
d = {}  # 定义一个空字典
for i in result1:
    if i not in d.keys(): # 如果这个元素不在字典的键里面 表示他是第一次出现
        d[i] = 1   # 将第一次出现的单词作为字典的键 出现次数作为字典值  The:1
    else: # 第二次或者多次出现
        d[i] += 1 # 每出现一次我就进行加一

print(d)

# 增加一个思考题
# 我想知道字典里面到底有多少个单词(要进行去重的)


# list1 = []
# # 返回的是字典键
# for i in d:
#     list1.append(i)
# # 取统计列表的长度我就知道有多少个单词
# print(len(list1))






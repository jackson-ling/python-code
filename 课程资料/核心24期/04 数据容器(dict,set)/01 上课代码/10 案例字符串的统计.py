"""
统计Python之禅中所有字符出现的次数
"""
# python 之禅
this_str = """
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
# 思路
# 你如果想去统计单词
# 去除里面的一些特殊字符
# split给他们分割成一个一个单词

"""
    统计Python之禅中所有字符出现的次数  python是严格区分大小写的 所以 T 和t 是表示2个不同字符

        1. 获取所有的字符
        2. 统计字符出现的次数
        
"""
# 统计函数 count  我现在都不知道哪些字符需要统计 这个方法是很鸡肋的


d = {} # 定义一个空的字典
for i in this_str: # 遍历字符串里面的每一个字符
    if i not in d.keys(): # 如果遍历出来的字符不在字典的键里面,就代表这个字符在字典中是第一次出现的
        d[i] = 1  # 字符本身作为一个键 出现次数作为值 a = 1  ---> a: 1 代表出现一次
    else:
        d[i] += 1  # a : 2 赋值运算 多次出现 后面每出现一次就加一 就可以统计每一个字符出现的次数

print(d)
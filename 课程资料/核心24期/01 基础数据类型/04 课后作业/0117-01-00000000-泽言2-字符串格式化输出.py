"""
请用一个字符串模板（三种格式化），输出以下结果
（只要能实现效果就行，不限制实现方式）

python 是一门动态解释型语言，起源于1989年圣诞节期间
Java 是一门静态编译型语言，起源于1991年
C 是一门静态编译型语言，起源于1969年到1973年期间
"""
s1 = "{} 是一门{}语言，起源于{}年{}"

"""自己在下方编写代码实现功能"""

# # 第一种格式:f搭配{}
# name='python'
# type='动态解释型'
# time='1989'
# jieduan='圣诞节期间'
# print(f'{name} 是一门{type}语言，起源于{time}年{jieduan}')
#
# # 第二种格式；format型
# name='java'
# type='静态编译型'
# time='1991'
# print('{} 是一门{}语言，起源于{}'.format(name,type,time))
#
# # 第三种格式；%s
# name='C'
# type='静态编译型'
# time1='1969'
# time2='1973'
#
# print('%s是一门%s语言，起源于%s至%s期间'%(name,type,time1,time2))


# 尝试使用列表索引一次性输出
language='python,java,C'
# print(language.split())
name=language.split(',')
print(name)
# name1="，".join(name)
# print(name1)
result=name[0]
print(result)
type='动态解释型'
time='1989'
jieduan='圣诞节期间'
print(f'{result} 是一门{type}语言，起源于{time}年{jieduan}')


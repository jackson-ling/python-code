#  len() 函数

# 通过len()函数计算字符串的长度时，
# 不区分英文、数字、汉字以及符号，
# 所有字符都按一个字符计算。

print(len("人生苦短,我用Python") )		# 13


#-----------------------------------------------------------------------------------------------------------


#count()函数   统计字符串中出现一个对象的次数（格式：变量.count(对象)）
a = '我爱北京天安门，天安门上太阳升'

print(a.count("天安门"))    # 2



#-----------------------------------------------------------------------------------------------------------


#find()函数    查找对象的‘’索引值‘’（不存在返回-1）
#（格式：变量.find(对象)）
a='1231'
print(a.find('1'))#返回第一次出现的位置索引值
print(a.rfind('1'))#返回最后一次出现的位置索引值
print(a.find('a'))#不存在返回-1


#-----------------------------------------------------------------------------------------------------------


#join()函数    格式：连接字符.join(序列)

print("--".join("我就是喜欢这么说话你来打我啊！"))
# 我--就--是--喜--欢--这--么--说--话--你--来--打--我--啊--！

# 序列也可以是其他的数据类型（比如：列表）
print(" ".join(["just","do","it"])) 	# just do it


#-----------------------------------------------------------------------------------------------------------

#split()分割
'''
1.在空白处分割
2.返回一个   ‘’列表‘’
3.如果指定字符分割，分割后去除该字符，如要保留，运用partition（）函数，并且返回的是元组类型
'''
#空白处分割
a='123 456'
b=a.split()
print(b)

#指定位置分割
s1 = "123哈 254哈 354534哈 4646"

li2 = s1.split("哈")
print(li2)				# ['123', ' 254', ' 354534', ' 4646']

#-----------------------------------------------------------------------------------------------------------
#指定字符分割并保留该字符
s1 = "123哈 254哈 354534哈 4646"

li2 = s1.partition("哈")
print(li2)				#  ('123', '哈', ' 254哈 354534哈 4646')
#-----------------------------------------------------------------------------------------------------------

#指定分割次数
s1 = "123哈 254哈 354534哈 4646"

li3 = s1.split("哈",2)
print(li3)			# ['123', ' 254', ' 354534哈 4646']

#右边开始分割（加一个r，区别rfind（）--返回最后一个）
li4 = s1.rsplit("哈",2)
print(li4)			# ['123哈 254', ' 354534', ' 4646']




#-----------------------------------------------------------------------------------------------------------


#splitlines()函数   在空白处分割，以行分割
a ="我说你是人间的四月天\r笑响点亮了四面风\r\n轻灵在春的光艳中交舞着变\n你是四月早天里的云烟\n黄昏吹着风的软\n星子在无意中闪\n细雨点洒在花前 \n你是一树一树的花开\n是燕在梁间呢喃，——你是爱，是暖\n是希望，你是人间的四月天！"

print(a.splitlines())
#和用split（）是一样的效果

"""
['我说你是人间的四月天',
 '笑响点亮了四面风',
 '轻灵在春的光艳中交舞着变',
 '你是四月早天里的云烟',
 '黄昏吹着风的软',
 '星子在无意中闪',
 '细雨点洒在花前 ',
 '你是一树一树的花开',
 '是燕在梁间呢喃，——你是爱，是暖',
 '是希望，你是人间的四月天！']
"""


#保留转义字符，在括号内加True---只适用splitlines()函数
b = a.splitlines(True)
print(b)

"""
['我说你是人间的四月天\r',
 '笑响点亮了四面风\r\n',
 '轻灵在春的光艳中交舞着变\n',
 '你是四月早天里的云烟\n',
 '黄昏吹着风的软\n',
 '星子在无意中闪\n',
 '细雨点洒在花前 \n',
 '你是一树一树的花开\n',
 '是燕在梁间呢喃，——你是爱，是暖\n',
 '是希望，你是人间的四月天！']
"""


#-----------------------------------------------------------------------------------------------------------

# replace（）函数   格式：字符串.replace(被替换的字符, 用来替换的字符, 替换次数)
print("人生苦短，我用python,python,pthon".replace("python","java",1))
# 人生苦短，我用java,python,pthon

# -----------------------------------------------------------------------------------------------------------

#strip（）函数    注意：可以连续使用
'''
功能：
删除str字符串两端的空白字符以及特殊字符
这里的特殊字符包括制表符\t、回车符\r、换行符\n
'''

# 只能去除两端，不能去除中间
c = " \r 哈哈哈%%\t\r哈哈哈\r\n"
print(c.strip())       # 哈哈哈%%\t\r哈哈




# 如果指定去除字符左右两边某些字符，在strip()内填入你指定的字符即可。
d = "@@@哈哈￥￥"
print(d.strip("@"))					# 哈哈￥￥
print(d.strip("@").strip("￥")) 		# 哈哈



# 字符串.rstrip()——只去除右边的空格和特殊字符
# 字符串.lstrip()——只去除左边的空格和特殊字符

e = '\n哈哈\t  '
print(e.lstrip()) 		# 哈哈\t
print(e.rstrip())		# \n哈哈
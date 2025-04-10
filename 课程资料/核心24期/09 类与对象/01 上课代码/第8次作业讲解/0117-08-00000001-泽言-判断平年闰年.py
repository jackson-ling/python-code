"""
判断平年闰年：

	闰年的条件是: 满足其中一个条件就行
		一:能被4整除，但不能被100整除的年份(例如2008是闰年，1900不是闰年) 
		二:能被400整除的年份(例如2000年)也是闰年。
	
	反之都是平年。
	
请设计一个函数 def

	用户输入年份，传入函数中的参数  input

	在函数中判断输入的年份是平年还是闰年
"""
# python2  <>
# python 3  !=   不等于

# 条件的判断

def max_year(year): # year是后面调用函数传递过来的数据
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f'{year}是闰年')
    else:
        print(f'{year}不是闰年')

# 调用函数去执行代码逻辑
# input 默认返回的是str类型 但是 数学运行是针对数值类型的
year = int(input('请输入你的年份:'))
max_year(year)




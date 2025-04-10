"""
判断平年闰年：

	闰年的条件是: 满足其中一个条件就行
		一:能被4整除，但不能被100整除的年份(例如2008是闰年，1900不是闰年) 
		二:能被400整除的年份(例如2000年)也是闰年。
	
	反之都是平年。
	
请设计一个函数
	用户输入年份，传入函数中的参数
	在函数中判断输入的年份是平年还是闰年
"""

def year_judge():
    global flag
    year = int(input('请输入要判断的年份：'))
    if year == -1:
        flag = 0
        return flag
    elif (year%4==0 and year%100!=0) or (year%400 == 0):
        flag = 1
        print(f'{year}是闰年')
        return flag
    else:
        flag = 1
        print(f'{year}是平年')
        return flag

flag = 1
while(flag):
    year_judge()
    if flag == 0:
        break
print('退出了')







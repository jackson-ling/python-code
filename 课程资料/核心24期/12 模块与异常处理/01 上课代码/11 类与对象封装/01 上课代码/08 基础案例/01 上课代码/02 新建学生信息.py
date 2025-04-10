"""
选择什么数据类型保存学生数据:  用户可以选择 **修改** 或者 **删除** 信息
      字典  列表  集合(pass)  元组(pass)
      如果涉及到数据的查找   字典  通过一个键值对一一对应
      综合所诉  报错数据  我们选择 字典
      {} {} {} {} {} {}
      针对对系统:
      使用到列表

      最终可以得到数据容器:[{},{},{},{},{},{}]

"""

# 1. 需要记录学生的 姓名、语文成绩、数学成绩、英语成绩、总分
name = input('请输入学生的姓名:')
chinese = int(input('请输入学生的语文成绩: '))
math = int(input('请输入学生的数学成绩: '))
english = int(input('请输入学生的英语成绩: '))
total = chinese + math + english
print(total)

students = [
    {'name':name,'chinese':chinese,'math':math,'english':english,'total':total}
]
print(students)
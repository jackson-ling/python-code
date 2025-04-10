"""
 选择什么数据类型保存学生数据:     用户可以选择 **修改** 或者 **删除** 信息
      字典 列表 集合(pass) 元组(pass)
      针对学生肯定是要方便快速查询自己的成绩,   字典 key:values (查找这种方法是最快也最准确的) 通过字典键的唯一性

针对学生而言:   {},{},{} 每一个字典就代表一个学生的信息
针对系统而言:  []列表
综合而言:  [{},{},{}]


"""
# 1. 需要记录学生的 姓名、语文成绩、数学成绩、英语成绩、总分
# 我现在只是去讲解他的思路  一些小瑕疵需要你们自己进行细节处理的
name = input('请输入你的名字:')
chinese = int(input('请输入你的语文成绩:'))
math = int(input('请输入你的数学成绩:'))
english = int(input('请输入你的英语成绩:'))

total = chinese + math + english # 总分成绩

students = [
    {'name':name,'chinese':chinese,'math':math,'english':english,'total':total,}
]
print(students)
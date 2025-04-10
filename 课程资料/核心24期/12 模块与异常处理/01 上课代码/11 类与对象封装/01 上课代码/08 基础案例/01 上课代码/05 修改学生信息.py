students = [
    {'name': '丸子', 'chinese': 12, 'math': 86, 'english': 86, 'total': 258},
    {'name': '正心', 'chinese': 12, 'math': 86, 'english': 86, 'total': 258},
    {'name': '巳月', 'chinese': 12, 'math': 86, 'english': 86, 'total': 258},
    {'name': '自游', 'chinese': 12, 'math': 86, 'english': 86, 'total': 258},
]
# 输入学生的姓名, 用于查找
modify_name = input('请输入你要修改的学生姓名:')
for stu in students:
    if stu['name'] == modify_name:

        name = input('请重新输入学生的姓名:')
        chinese = input('请重新输入学生的语文成绩: ')
        math = input('请重新输入学生的数学成绩: ')
        english = input('请重新输入学生的英语成绩: ')

        if name:  # 空字符串的布尔判断结果为False
            stu['name'] = name
        if chinese:
            stu['chinese'] = int(chinese)
        if math:
            stu['math'] = int(math)  # 指定键修改值
        if english:
            stu['english'] = int(english)  # 指定键修改值
        stu['total'] = stu['chinese'] + stu['math'] + stu['english']


        break
else:  # 当循环正常结束的时候 else会被执行
    print('该学生不存在, 请检查名字是否输入正确!')


print(students)



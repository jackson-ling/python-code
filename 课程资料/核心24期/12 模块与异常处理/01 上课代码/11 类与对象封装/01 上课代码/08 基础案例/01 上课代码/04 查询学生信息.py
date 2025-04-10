students = [
    {'name': '丸子', 'chinese': 12, 'math': 86, 'english': 86, 'total': 258},
    {'name': '正心', 'chinese': 12, 'math': 86, 'english': 86, 'total': 258},
    {'name': '巳月', 'chinese': 12, 'math': 86, 'english': 86, 'total': 258},
    {'name': '自游', 'chinese': 12, 'math': 86, 'english': 86, 'total': 258},
]

# 输入学生的姓名, 用于查找
search_name = input('请输入你要查询的名字:')
for stu in students:
    # 如果遍历的学生字典中名字是要查找的学生姓名
    if stu['name'] == search_name:# 满足的条件
        print('姓名\t语文\t数学\t英文\t总分')
        print(f"{stu['name']}\t{stu['chinese']}\t{stu['math']}\t{stu['english']}\t{stu['total']}")  # \t是一个制表符
        break
else:# 当循环正常结束的时候 else会被执行
    print('该学生不存在, 请检查名字是否输入正确!')




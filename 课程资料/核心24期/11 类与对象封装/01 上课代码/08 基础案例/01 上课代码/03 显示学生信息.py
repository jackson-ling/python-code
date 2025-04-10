students = [
    {'name': '丸子', 'chinese': 86, 'math': 86, 'english': 86, 'total': 258},
    {'name': '正心', 'chinese': 86, 'math': 86, 'english': 86, 'total': 258},
    {'name': '巳月', 'chinese': 86, 'math': 86, 'english': 86, 'total': 258},
    {'name': '自游', 'chinese': 86, 'math': 86, 'english': 86, 'total': 258},
]
print('姓名\t语文\t数学\t语文\t总分')
for stu in students:
    # print(stu)
    # 只能是但包双 或者双包单 不能是单包单 或者双包双
    print(f"{stu['name']}\t{stu['chinese']}\t\t{stu['math']}\t\t{stu['english']}\t\t{stu['total']}")
    # \t代表制表符
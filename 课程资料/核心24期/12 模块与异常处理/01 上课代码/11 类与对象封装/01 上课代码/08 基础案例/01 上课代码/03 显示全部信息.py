students = [
    {'name': '丸子', 'chinese': 12, 'math': 86, 'english': 86, 'total': 258},
    {'name': '正心', 'chinese': 12, 'math': 86, 'english': 86, 'total': 258},
    {'name': '巳月', 'chinese': 12, 'math': 86, 'english': 86, 'total': 258},
    {'name': '自游', 'chinese': 12, 'math': 86, 'english': 86, 'total': 258},
]

print('姓名\t语文\t数学\t英文\t总分')
for stu in students:
    print(f"{stu['name']}\t{stu['chinese']}\t\t{stu['math']}\t\t{stu['english']}\t\t{stu['total']}")  # \t是一个制表符

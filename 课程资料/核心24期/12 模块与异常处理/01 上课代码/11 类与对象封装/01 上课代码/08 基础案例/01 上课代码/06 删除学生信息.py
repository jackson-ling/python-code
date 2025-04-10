students = [
    {'name': '丸子', 'chinese': 12, 'math': 86, 'english': 86, 'total': 258},
    {'name': '正心', 'chinese': 12, 'math': 86, 'english': 86, 'total': 258},
    {'name': '巳月', 'chinese': 12, 'math': 86, 'english': 86, 'total': 258},
    {'name': '自游', 'chinese': 12, 'math': 86, 'english': 86, 'total': 258},
]

# 输入学生的姓名, 用于查找
del_name = input('请输入您要查询的学生姓名: ')
for stu in students:
    # 如果遍历的学生字典中名字是要查找的学生姓名
    if stu['name'] == del_name:
        # pop(默认是删除最后一个列表数据, 也可以指定索引在列表中删除数据)
        # remove(根据数据在列表中删除)
        students.remove(stu)
        # students.pop(students.index(stu))
        break
else:
    print('该学生不存在, 请检查名字是否输入正确!')
print(students)



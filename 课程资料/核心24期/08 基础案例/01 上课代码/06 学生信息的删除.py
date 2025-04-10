students = [
    {'name': '丸子', 'chinese': 86, 'math': 86, 'english': 86, 'total': 258},
    {'name': '正心', 'chinese': 86, 'math': 86, 'english': 86, 'total': 258},
    {'name': '巳月', 'chinese': 86, 'math': 86, 'english': 86, 'total': 258},
    {'name': '自游', 'chinese': 86, 'math': 86, 'english': 86, 'total': 258},
]

# 输入名字去查找删除的对象
del_name = input('请输入你要删除的名字:')
for stu in students:
    if stu['name'] == del_name: # 表示已经成功找到了
        # pop(默认是删除最后一个列表数据, 也可以指定索引在列表中删除数据)
        # students.pop(students.index(stu))   # 获得索引 通过索引删除
        # remove(根据数据在列表中删除)
        students.remove(stu) # 通过删除指定数据 这种方法是最简单的
        # del stu  后面跟的是索引或者列表的名字
        break
else:
    print('该学生不存在, 请检查名字是否输入正确!')

print(students)


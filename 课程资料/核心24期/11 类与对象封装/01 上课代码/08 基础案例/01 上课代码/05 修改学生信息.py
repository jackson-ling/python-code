students = [
    {'name': '丸子', 'chinese': 86, 'math': 86, 'english': 86, 'total': 258},
    {'name': '正心', 'chinese': 86, 'math': 86, 'english': 86, 'total': 258},
    {'name': '巳月', 'chinese': 86, 'math': 86, 'english': 86, 'total': 258},
    {'name': '自游', 'chinese': 86, 'math': 86, 'english': 86, 'total': 258},
]

# 输入学生的姓名, 用于修改
modify_name = input('请输入你要修改的名字:')
for stu in students:
    # 方法二   (如果遇到不想修改的信息 敲回车跳过)
    if stu['name'] == modify_name:  # 表示成功找到了数据
        print('不想修改改内容,请敲回车跳过')  # 此时敲的回车就相当于一个空字符
        name = input('请重新输入你的名字:')
        chinese = input('请重新输入你的语文成绩:') # int不能对空字符强转
        math = input('请输重新入你的数学成绩:')
        english = input('请重新输入你的英语成绩:')

        if name: # 非空即使true   空字符串的布尔判断结果为False 使用自己原来的名字
            stu['name'] = name   # 通过字典键覆盖去达到修改的目的
        if chinese: # 非空即使true   空字符串的布尔判断结果为False
            stu['chinese'] = int(chinese)   # 通过字典键覆盖去达到修改的目的
        if math: # 非空即使true   空字符串的布尔判断结果为False
            stu['math'] = int(math)   # 通过字典键覆盖去达到修改的目的
        if english: # 非空即使true   空字符串的布尔判断结果为False
            stu['english'] = int(english)   # 通过字典键覆盖去达到修改的目的
        # 总分应该是前面的数据重新覆盖更新之后再去计算
        stu['total'] = stu['chinese'] +  stu['math'] + stu['english']
        break
# 没有找到
else:
    print('该学生不存在, 请检查名字是否输入正确!')
print(students)
#
# if stu['name'] == modify_name:  # 就表示数据找到了
#     # 方法一  # 通过重新赋值去达到修改的目的
#     name = input('请重新输入你的名字:')
#     chinese = int(input('请重新输入你的语文成绩:'))
#     math = int(input('请输重新入你的数学成绩:'))
#     english = int(input('请重新输入你的英语成绩:'))
#
#     total = chinese + math + english  # 总分成绩
#
#     # 通过字典键覆盖去达到修改的目的
#     stu['name'] = name
#     stu['chinese'] = chinese
#     stu['math'] = math
#     stu['english'] = english
#     stu['total'] = total
#     break  # 退出for循环 因为已经找到了 所以后面的就不要再遍历了

import json

students = [
    {'name': '丸子', 'chinese': 86, 'math': 86, 'english': 86, 'total': 258},
    {'name': '正心', 'chinese': 86, 'math': 86, 'english': 86, 'total': 258},
    {'name': '巳月', 'chinese': 86, 'math': 86, 'english': 86, 'total': 258},
    {'name': '自游', 'chinese': 86, 'math': 86, 'english': 86, 'total': 258},
]




# 在整个系统对学生进行增删改查操作的时候需要的是 [{}, {}, {}] 列表
# # 当我们进入系统的时候是需要对原来有的数据进行加载的
# with open('students.json',mode='r',encoding='utf-8') as f:
#     student_s = f.read() #  # 使用read方法读取的是str类型数据
#     print(student_s)
#     print(type(student_s))
#
# # 因为我是在操作列表的增删改查 但是现在返回的是str  需要将str 变成 列表类型
# students1 = json.loads(student_s) # 将str转化为列表类型
# print(students1)
# print(type(students1))

# 当退出系统的时候需要把数据保存到文件里面去
with open('students.json',mode='w',encoding='utf-8') as f:
    # write只能写入 二进制和str
    # f.write(str(students)) # 这种方法是不行的 # 如果使用str强转 那么保存的不睡json类型的数据 在后的操作和取值是会有问题
    # 这个是因为json在进行序列化时，默认使用的是编码SCAII，而中文为Unicode编码，ASCII中不包含中文，所以出现了乱码。
    # 在我们保存的时候需要把list列表类型转化成str类型
    # ensure_ascii = False 表示不去使用编码SCAII 让中文可以正常显示
    students_str = json.dumps(students,ensure_ascii=False) # 将列表数据变回str类型
    print(students_str)
    print(type(students_str))
    f.write(students_str)


# json后缀的是专门用于保存json数据(双引号的)  字典型数据(单双都可以的)
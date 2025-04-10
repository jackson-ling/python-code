students = [
    {'name': '丸子', 'chinese': 86, 'math': 86, 'english': 86, 'total': 258},
    {'name': '正心', 'chinese': 86, 'math': 86, 'english': 86, 'total': 258},
    {'name': '巳月', 'chinese': 86, 'math': 86, 'english': 86, 'total': 258},
    {'name': '自游', 'chinese': 86, 'math': 86, 'english': 86, 'total': 258},
]
# print(type(students))
import json
# 当退出系统的时候需要把数据保存到文件里面去
# 这个是因为json在进行序列化时，默认使用的是编码SC是AII，而中文为Unicode编码，ASCII中不包含中文，所以出现了乱码。
# with open('students.json',mode='w',encoding='utf-8') as f:
#     # 字符串和二进制
#     # f.write(str(students))  #不建议使用str强转
#
#     # 列表类型转字符串
#     # ensure_ascii=False  不使用默认的编码 让他正常显示中文
#     student_str = json.dumps(students,ensure_ascii=False)
#     # print(student_str)
#     # print(type(student_str))
#     f.write(student_str)

# 同学们要注意当我们进入系统的时候是不是要进行数据的读取
# 在整个系统对学生进行增删改查操作的时候需要的是 [{}, {}, {}] 列表

with open('students.json',mode='r',encoding='utf-8')as f:
    student_str = f.read()
    print(student_str)
    print(type(student_str))

students1 = json.loads(student_str) # 将字符串转化为python对象
print(students1)
print(type(students1))



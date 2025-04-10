students = [
    {'name': 'TOM', 'age': 20},
    {'name': 'ROSE', 'age': 19},
     {'name': 'Jack', 'age': 22}
]
# sort 冒泡排序  他们涉及的第一个序列只有数字 [3, 38, 44, 5, 47, 15, 36, 26]
# sort实现对序列的排序
# students.sort()
# print(students)
# 既然这个字典不能够排序 那么我只需要通过字典里面的age键来排序


def age(x1):
    # print(x1)
    return x1['age']  # 此时他就会在底层对age字段进行比较然后在排序
    # return x1
# # key参数后指定一个函数名的
# 会把 students 列表每一个数据传入到指定的函数当中作为实际参数   在底层会遍历传递给x1
students.sort(key=age,reverse=True)
print(students)



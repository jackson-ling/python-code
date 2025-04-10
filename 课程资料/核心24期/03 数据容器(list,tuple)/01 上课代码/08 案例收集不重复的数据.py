# 收集以下列表中所有不重复的数据
# 进行去重 集合强转是可以的后面会讲的 集合的自动去重）

# list1 = [4, 2, 1, 0, 6, 2, 1]
# a = set(list1)
# print(list(a))
# list2 = [] # 定义空的列表
# for i in list1:
#     # print(i)
#     if i not in list2: # 如果数据不存在则添加到列表(第一次出现的数据肯定不在空列表里面)
#         list2.append(i)
#     else: # 第二次出现的数据
#         pass   #如果什么都不想做就使用pass(占位符）
# print(list2)

# 收集以下列表中所有不重复的数据, 找重复数据的索引
# list3 = [4, 2, 1, 0, 6, 2, 1]
# list4 = []
# for i in range(len(list3)): # 0123456
#     if list3[i] not in list4:  # 如果数据不存在 通过下标索引取值
#         list4.append(list3[i])# 如果数据不存在则添加到列表(第一次出现的数据肯定不在空列表里面)
#     else:  # 第二次出现的数据
#         print(i) # 这个就是重复索引
# print(list4)






# 收集不重复数据
list=[1,2,3,3,4]
list1=[]
for i in range(len(list)):
    if list[i] not in list1:
        list1.append(list[i])
    else:
        print(f'重复出现的数据索引是：{i}')
print(list1)

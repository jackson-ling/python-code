# max 求一个序列的最大值
# min 求一个序列的最小值
# sum 求一个序列的和

# a = [1,3,4,5,6,7,8]
# print(max(a))
# print(min(a))
# print(sum(a))

# """
# 编写一个函数，计算传入的数值序列的最大值、最小值和平均值，并一起返回，然后调用该函数
# """
## 自己写的逻辑
# def get_num(arr):
#     # print(arr)
#     """求最小值"""
#     min_num = arr[0]  # 假设他是最小
#     for i in arr:  # 遍历列表
#         if i < min_num:  # 判断
#             min_num = i  # 重新赋值最小值
#     """求最大值"""
#     max_num = arr[0]  # 假设他是最大
#     for j in arr:
#         if j > max_num:
#             max_num = j
#
#     """平均值"""
#     total = 0
#     for k in arr:
#         total += k # 求序列的总和
#     average_num = total/len(arr)
#     return min_num,max_num,average_num
#
#
# # 调用函数传递参数
# print(get_num([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]))

# 内置函数方法
def gert_num1(arr):
    min_num = min(arr)
    max_num = max(arr)
    average_num = sum(arr)/len(arr)
    return min_num,max_num,average_num
print(gert_num1([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]))
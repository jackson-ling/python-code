#方法一：运用循环遍历
a=int(input())
b=[int(i) for i in input().split()]
min_num = b[0]  # 假设他是最小
for i in b:  # 遍历列表
    if i < min_num:  # 判断
            min_num = i  # 重新赋值最小值
print(min_num)


#方法二：使用内置函数(对象是一个序列)
# max 求一个序列的最大值
# min 求一个序列的最小值
# sum 求一个序列的和
a=int(input())
b=[int(i) for i in input().split()]
print(min(b))
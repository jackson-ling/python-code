'''
例子：读入一个3行4列的二维矩阵

0 0 0 255
0 0 255 0
0 30 255 255
'''

# 输入第一行：行数 n 和列数 m
n, m = map(int, input().split())

# 初始化矩阵
matrix = []

#录入
for i in range(n):#循环n次，实现录入n行的操作
    li=[int(i) for i in input().split()]
    #或者使用下面的，比较常见
    # row = list(map(int, input().split()))
    matrix.append(li)

# 打印矩阵内容

#方式一：本身就是列表，用解包运算符（*）实现空格分隔输出

print("\n矩阵内容为:")
for i in matrix:
    print(*i)

#方式二：较为常用，利用字符串和join

# print("\n矩阵内容为:")
# for row in matrix:
#     print(" ".join(map(str, row)))  # 将每行的元素用空格连接为字符串并打印

#方法三：遍历每一个元素，控制输出格式
matrix = [[1, 2], [2, 3], [3, 2]]
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
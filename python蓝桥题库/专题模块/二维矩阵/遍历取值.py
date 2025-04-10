# 生成一个二维列表，3行4列
n = 3  # 行数
m = 4  # 列数

# 生成二维列表   (i * m + j)根据数学关系依次生成了0-11
matrix = [[(i * m + j) for j in range(m)] for i in range(n)]

# 打印生成的二维列表
print("生成的二维列表:")
for row in matrix:
    print(row)


# 遍历二维列表，按坐标的形式打印出每个元素
print("\n遍历二维列表:")

for i in range(n):         # 遍历每一行
    for j in range(m):     # 遍历每一列
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")


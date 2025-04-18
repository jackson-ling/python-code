# n行m列
n,m=map(int,input().split())

#实现二维矩阵录入
a=[] #用一个列表存入已录入的矩阵
for i in range(n):#循环n次，即n行
   li=[int(i) for i in input().split()]
   a.append(li)

#生成一个二维矩阵输出答案
b=[[0]*m for i in range(n)]


#生成一个方向数组，代表坐标的变化（注意：x是行的变化，y是列的变化）
dir = [
    (0, 1),   # 右 (当前格子右侧)
    (0, -1),  # 左 (当前格子左侧)
    (-1, 0),  # 上 (当前格子上方)
    (1, 0),   # 下 (当前格子下方)
    (-1, -1), # 左上 (当前格子的左上角)
    (-1, 1),  # 右上 (当前格子的右上角)
    (1, -1),  # 左下 (当前格子的左下角)
    (1, 1)    # 右下 (当前格子的右下角)
]


#遍历每一个位置(先遍历行，在遍历列)
for i in range(n):
   for j in range(m):
      if a[i][j]==1:
          b[i][j]=9  #如果当前格子有地雷，这个位置的结果就输出9
      else:
        b[i][j]=0   #如果当前格子没有地雷，先置为0，后面通过计算周围地雷的数量后再重新赋值
                    #当然这里多余了，前面已经设置了，这里只是为了方便理解
        for k in range(8):#遍历8个方向，在下标索引中通过k拿到变化的方向，通过x，y拿到变化量
            x=i+dir[k][0]
            y=j+dir[k][1]
            #重要的来了，要判断是否越界
            if 0<=x<n and 0<=y<m:
                b[i][j]+=a[x][y]

'''
补充一下除了用方向数组遍历方向的变化，还可以遍历x，y的增量

方法二：嵌套循环（注意需要判断是否是原点）
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:  # 如果当前格子是地雷
            b[i][j] = 9
        else:  # 计算周围地雷数
            for delta_x in [-1, 0, 1]:  # 遍历行的偏移量
                for delta_y in [-1, 0, 1]:  # 遍历列的偏移量
                    if delta_x == 0 and delta_y == 0:
                        continue  # 跳过当前格子本身
                    x = i + delta_x  # 计算相邻格子的行坐标
                    y = j + delta_y  # 计算相邻格子的列坐标
                    if 0 <= x < n and 0 <= y < m:  # 检查是否越界
                        b[i][j] += a[x][y]  # 累加周围的地雷数


'''


#最后输出一下答案
for i in b:
    print(*i) #可以使用这种比较简洁，本身就是数组，用*（解包）就可以实现输出用空格隔开


'''
补充一下常用的套路：如何输出二维矩阵(字符串的join)
for i in b:
  print(' '.join(map(str,i)))
'''
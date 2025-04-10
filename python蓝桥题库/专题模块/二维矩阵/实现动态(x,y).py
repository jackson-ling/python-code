#注意：一般在实现动态的方向变化后，还要判断是否越界，再去满足题目要求



#方法一：设置方向数组
dir = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
for k in range(8):#遍历八个方向，以一个点为中心，周围一圈包围了中心点
    x = 2 + dir[k][0] # 0 代表每个偏移方向中的x，即行数x（坐标上纵向的变化）的变化量
    y = 2 + dir[k][1] # 1 代表每个偏移方向中的y，即列数y（坐标上横向的变化）的变化量
    print(f"方向 {k}: x={x}, y={y}")

'''
例子
1 1 1
1 x 1
1 1 1 
'''

#结果
'''
方向 0: x=2, y=3   # 右
方向 1: x=2, y=1   # 左
方向 2: x=1, y=2   # 上
方向 3: x=3, y=2   # 下
方向 4: x=1, y=1   # 左上
方向 5: x=1, y=3   # 右上
方向 6: x=3, y=1   # 左下
方向 7: x=3, y=3   # 右下
'''


#方法二：嵌套循环（注意需要判断是否是原点）
for delta_x in [-1, 0, 1]:
    for delta_y in [-1, 0, 1]:
        if delta_x == 0 and delta_y == 0:
            continue  #如果偏移量是0，就表示还在原点，原点不是所需偏移的方向，跳过这一次，不会生成偏移后新方向的坐标
        x = 2 + delta_x
        y = 2 + delta_y
        print(f"delta_x={delta_x}, delta_y={delta_y}: x={x}, y={y}")


#结果
'''
delta_x=-1, delta_y=-1: x=1, y=1   # 左上
delta_x=-1, delta_y=0:  x=1, y=2   # 上
delta_x=-1, delta_y=1:  x=1, y=3   # 右上
delta_x=0, delta_y=-1:  x=2, y=1   # 左
delta_x=0, delta_y=1:   x=2, y=3   # 右
delta_x=1, delta_y=-1:  x=3, y=1   # 左下
delta_x=1, delta_y=0:   x=3, y=2   # 下
delta_x=1, delta_y=1:   x=3, y=3   # 右下

'''
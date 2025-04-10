#说明：n行m列，每个元素对应（x,y），x表示行，y表示列，先遍历行后遍历列


# 注意：第一行第一个元素的下标索引是li[0][0],第0行第0列


#方法一:生成n行m列的二维矩阵

# n,m=map(int,input().split())
n=4
m=5
li=[[0]*m for i in range(n)] #这里使用列表乘法，和下面for循环等价
li[0][2]=5
print(li)
print(li[0][2])

'''
[[0, 0, 5, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
5
'''

#方法二：生成a行b列的二维矩阵

a,b=map(int,input().split())
li2= [[0 for j in range(b)] for k in range(a)]

#方法三：生成x行y列的二维矩阵

x,y=map(int,input().split())
li3=[]
for i in range(x):
    li3.append([0 for j in range(y)])


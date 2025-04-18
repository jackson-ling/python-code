'''
题目：给一个数字x，将其拆分成n个正整数，后一个要求大于等于前一个，给出方案

思路：采用枚举，列出树状图，一层层搜索
'''

def dfs(depth):

    # 先写递归出口，同时判断是否符合题目要求

    # n的解释：先拆分成（1，x），再对每个数字继续拆成（1，x），这个过程才算一重循环，
    #         即第一次拆分算第0重循环，那n就表示最后一重循环下面的那一层，也就是递归出口

    if depth==n:  # 找到搜索的每一层

        # 到了某一层之后需要判断是否符合题目条件，即要求拆分的数：后一个大于前一个

        for i in range(1,n):  # 用了数组记录方案，这里的表示遍历数组中的每一个数字
            if path[i-1]<=path[i]:
                continue   # 如果符合题目条件，就什么也不做
            else:
                return

        if sum(path)!=x:
            return

        print(path)

        return   # 这里就是递归的出口

    # 对于每一层，枚举出当前拆分的数字
    for i in range(1,x+1):  # 左闭右开
        path[depth]=i  # 把每一层枚举的数记下来
        dfs(depth+1)  # 采用递归，方法都是一样的







x=int(input())
n=int(input())
path=[0]*n  # 用一个数组记录可行的路径
dfs(0)  # 从第0重循环开始往下搜索，即第一次拆分，之后才是对拆分的每个数字继续拆分成（1，x），这样进行组合判断

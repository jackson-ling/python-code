# 求根号二的值，无限二分，让结果更准确

'''
二分思路：确定一个区间，开始二分，然后判断是否合法（自己写一个函数），更新一次答案
'''

left,right=1,2
for i in range(100):
    mid=(left+right)/2
    if mid*mid>3:
        right=mid
    else:
        left=mid
    print(left,right)
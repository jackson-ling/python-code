'''
注意：对变量不确定且一直变化的可以用while循环，但注意是不是用死循环，while后面可以跟条件
'''

s=float(input())
step=2#第一步游2米
tot=0 #统计总距离
cnt=0#统计步数
# 接下来每一步只能游上一步的距离的0.98
# 问要游多少步?


# # 只要tot<s一直循环，知道满足条件退出循环
while tot<s:
   tot+=step
   step *= 0.98
   cnt+=1
print(cnt)


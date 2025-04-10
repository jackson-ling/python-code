# 性质1：是偶数
# 性质2：大于4且不大于12
# 小 A 喜欢这两个性质同时成立的整数
# Uim 喜欢这至少符合其中一种性质的整数
# 小 B 喜欢刚好有符合其中一个性质的整数
# 正妹喜欢不符合这两个性质的整数
# 如果喜欢则输出 1，否则输出 0

# 如果是输出0/1来判断结果的题目，可以先初始化定义值为0，再用if语句判断来对变量赋值

'''
纠正错误理解：如果条件是独立的，直接用多个if，如果条件有前提限制才用elif，代码运行逻辑是
从上到下的，如果条件相互独立用elif，那么就会执行if这个先前条件，
运行结果就和这个条件的独立性矛盾了
'''

#还有一种可能就是if的条件中有与条件符合的，但是又缺少了符合elif的条件，那么就会执行if的结果
x=int(input())
a=0
b=0
c=0
d=0
if x%2==0 and 4 < x <= 12:#表示小A
    a=1
if x%2==0 or 4 < x <= 12 or (x%2==0 and 4 < x <= 12):#表示Uim
    b=1
#至少，可以是一种或两种，而一种又有两种情况
if  (x%2==0 and x<=4 and x>12) or (x%2!=0 and 4 < x <= 12):
    c=1
#只满足一种，另一个条件不满足，那么这个不满足的条件就是满足这个条件的反面，就是他的补集
if (x%2!=0 and x<=4) or (x%2!=0 and x>12) :#表示正妹
    d=1
print(a,b,c,d)
import math
a,b=map(int,input().split())
#a是元
#b是角
money=a+b*0.1
pen_money=1.9
amount=money/pen_money
print(math.floor(amount))
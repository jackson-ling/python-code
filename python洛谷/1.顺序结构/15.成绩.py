#定义a：作业成绩，b：小测成绩，c：期末考试成绩
a,b,c=map(int,input().split())
number=a*0.2+b*0.3+c*0.5
print(int(number))
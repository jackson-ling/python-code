#这题很诡异，关键就在两个if，如果用if-elif的结构会出错

n=int(input())
li=[]
a=0
b=0
for i in range(n):
    mark=int(input())
    li.append(mark)
for i in li:
    if i>=60:
        a+=1
    if i>=85:
        b+=1
x=a/n
y=b/n

print(f'{x:.0%}')
print(f'{y:.0%}')
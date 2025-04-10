n=int(input())
li=[]
for i in range(1,n+1):
    if '1' in str(i) or '2' in str(i)  or '0' in str(i) or '9' in str(i):#注意是or 不是 and
        li.append(i)
print(sum(li)) #运用内置函数快速求和

#巧妙的方法
n = int(input())

sum = 0
for i in range(1, n + 1):
    for j in str(i):
        if j in '2019':
            sum += i
            break

print(sum)
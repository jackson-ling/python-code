#逻辑出现问题，忽略了取模结果为0的情况

a=int(input())
n=int(input())

if a+n>=8:
 if (a+n)%7==0:#n=0的情况
  print(7)
 else:
  print((a+n)%7)

elif a+n<=7:
 print(a+n)



#标答
w = int(input())
n = int(input())
x = (w+n)%7
if x == 0 :
    x = 7
print(x)
#运用所学的运算符，编写一个计算器
print("欢迎使用python编写的简单计算器，支持加减乘除")
print('输入一个字符表示计算方式：')
chr=input()
print('依次输入两个数字')
a=int(input('a='))
b=int(input('b='))
if chr=='+':
    print('a+b=',a+b,sep='')
elif chr=='-':
    print('a-b=',a-b,sep='')
elif chr=='*':
    print('a*b=',a*b,sep='')
elif chr=='/':
    print('a/b=',float(a)/float(b),sep='')

# 待解决：如何用循环实现持续输入
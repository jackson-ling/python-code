n=int(input())
num=1
for i in range(1,n+1):#外层循环，控制打印的行数
    for j in range(1,n+1):  # 内层循环，表示循环几次
        print('%02d' % num, end='')
        num+=1
    print()
print()
num=1
for i in range(1,n+1):

    # 方法一：字符串惩罚乘法打印空格
    # print('  '*(n-i),end='')#易错点：因为这里用0占位为了，所以空格要占位两个

    # # # 方法二：找规律用循环表达
    span = n - i
    for k in range(span):
        print('  ', end='')#易错点：因为这里用0占位为了，所以空格要占位两个

    for j in range(i):
        print('%02d'%num,end='')
        num+=1
    print()


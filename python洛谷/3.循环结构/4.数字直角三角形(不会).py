n=int(input())
num=1
for i in range(n,0,-1):#54321,外层循环，5行--确定遍历范围，循环五次，依次递减（步长是负值）
    for j in range(i):#内层循环，行数对应个数，变量范围一致（理解便利的过程）
        print('%02d'%num,end='')
        num+=1#表示循环打印的内容，是数的变化
    print()
#print（）表示输出完后换行
#格式化字符串：有多个变量可以采用%s格式
#填充：%02d（用0填充，长度为2）



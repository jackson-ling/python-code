"""
用for语句实现九九乘法表
# """
for i in range(1,10):
    for k in range(1,i+1):
        print(f'{k}*{i}={i*k}',end='\t')
    print()
#  while循环打印九九乘法表
i=1
while i<10:
    j=1
    while j<=i:
        print(f'{j}*{i}={j*i}', end='\t')  # \t他是一个制表符可以让数据整齐排列
        j += 1
    print()
    i+=1
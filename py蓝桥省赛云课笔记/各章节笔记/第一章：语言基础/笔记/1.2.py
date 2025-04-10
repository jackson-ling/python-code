#1.2  python输入输出

'''
print函数的两个参数(使用输出多个对象)

sep:代码之间默认以  空格  分割
end:代码结尾默认以  换行  结束

'''
print('a','b','c')
print('a','b','c',sep='')
print('a','b','c',sep='--')
print('a','b','c',sep='?')


print(123,end='--')  #就是以‘--’结尾
print()  #打印空字符，默认以换行结尾，即这个语句----表示  “换行“
print(123) #以换行结尾，最后进程结束的提示和123之间相差一行
# ----------------------------------------------------------------
print(123,end='--')
print(123)
# 结果  123--123



'''
input 函数
'''
# 默认都是录入 '字符串'，如果需要转换类型，需要强转

a=input()
b=int(input())
c=float(b)

#通过type函数去查看类型

print(type(a))
print(type(b))
print(type(c))


'''
区别C语言:
int i=5;
float j=i/2;
float k=(float)i/2;

'''


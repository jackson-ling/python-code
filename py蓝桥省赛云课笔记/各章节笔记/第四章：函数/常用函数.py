'''
1.lambda函数（可以快速定义一个函数并返回值）

lambda (参数)：(满足的条件或者函数需要执行的内容)

gg = lambda x,y : x + y
print(gg(5,6))       # 11



2.zip函数（可以理解为打包，并且是一一对应的，组合两个可迭代的序列，常用于列表，字符串）
          返回的是元组类型

注意：调用函数是一个过程，需要强转成list查看结果，或者用变量接收

a = [1,2,3,4,5]
b = "python123"
print(list(zip(a,b)))

# [(1, 'p'), (2, 'y'), (3, 't'), (4, 'h'), (5, 'o')]


结合for循环遍历

rank = ["第一","第二","第三"]
name = ["张三","李四","王五"]

for r,n in zip(rank,name):
    print(r+ " --> " + n)


第一 --> 张三
第二 --> 李四
第三 --> 王五



3.filter函数（过滤函数）
两种情况：1.第一个参数是函数，第二个是可迭代的数据类型，会把里面的参数带入函数计算并返回结果
         2.第一个是none或者0（假），第二个是可迭代的数据类型，会返回true的值

注意：调用函数是一个过程，需要强转成list查看结果，或者用变量接收

temp = filter(None,[1,2,0,False,True])

print(list(temp))		# [1, 2, True]

应用:筛选素数

def (写一个筛选素数的函数)：
     .......

print(list(filter(def,range(1,11))))


4.map函数

map（函数，可迭代序列）工作原理：
将序列的每一个个元素作为函数的参数进行运算加工，
直到可迭代序列每个元素加工完毕，返回所有加工后的元素构成的新序列

区别filter，filter返回的是其中的true值

常用：a,b,c=map(int,input().split())


5.enumerate函数：返回元素，元素对应的下标索引

注意：调用函数是一个过程，需要强转成list查看结果，或者用变量接收

s = "python"

print(list(enumerate(s)))

[(0, 'p'), (1, 'y'), (2, 't'), (3, 'h'), (4, 'o'), (5, 'n')]

结合for循环遍历：

li=list(range(5))
for x,y in enumerate(li):
print(x,y)

0 0
1 1
2 2
3 3
4 4
'''
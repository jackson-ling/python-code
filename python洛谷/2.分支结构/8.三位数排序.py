'''
纠正一个错误思维，题目要求的输入格式是要数字之间用空格隔开，
则附加使用split()函数即可，只要出现函数input（）即可,
那么我输入之后a，b以什么形式呈现无关紧要，可以是列表，字典，
之后如果果要单独出现用for循环去遍历即可
'''
list=[int(i) for i in input().split()]
list.sort()
for i in list:
    print(i,end=' ')


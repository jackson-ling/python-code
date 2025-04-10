#方法一：
word=input()
print(word.upper())

#方法二：用一行代码
#print(input().upper())

#方法三：传统方法，解释了upper（函数内部的构造），同时反映了可以使用字符判断存在范围的思路
'''

a = input()
for i in a:
    if 'a' <= i <= 'z':
        print(chr(ord(i) - 32), end='')
    elif 'A' <= i <= 'Z':
        print(i, end='')

'''


'''
拓展：
1. upper（）统一转成大写
2. lower（）统一转成小写
3. title（）将每个单词的首字母大写，其他字母小写
4. capitlize（）将首字母大写，其他字母小写

'''


'''
拓展：
1. upper（）统一转成大写
2. lower（）统一转成小写
3. title（）将每个单词的首字母大写，其他字母小写
4. capitlize（）将首字母大写，其他字母小写

'''
# 传统方法理解（统一转成大写为例）
a = input()
for i in a:
    if 'a' <= i <= 'z':
        print(chr(ord(i) - 32), end='')
    elif 'A' <= i <= 'Z':
        print(i, end='')


#速解题目
print(input().upper())



#chr（）函数和ord（）函数

print(ord('a'))  #97

print(chr(97))   #a

print(chr(ord('a')-32))   #A

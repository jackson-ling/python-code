f = open('t6.txt',mode='r',encoding='utf-8')
# print(f.readline(),end='') # 每一次只能读取一行数据  并没有读取换行符造成换行
# print(f.readline()) # 每一次只能读取一行数据
# print(f.readline(25)) # 也是按照字符长度进行读取 如果参数超过一行的字符数,那么就会把一行整个返回



#  我不知道我的文件到底有多少行? 我不知道要使用多少次readline方法

while True:
    txt = f.readline()
    if txt:  # 利用非空即使True    只要当txt是一个空的就表示已经全部的读取完毕了
        print(txt)
    else:
        break
f.close()


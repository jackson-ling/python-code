f = open('t6.txt',mode='r',encoding='utf-8') # 如果在读取文件汉字的时候出现了乱码问题
# utf-8和gbk但是有可能的 2个编码都试一下
print(f.read())  # 默认读取文件里面的所有内容
print(f.read(9)) # 这里读取的是字符长度 而不是字节(和编码方式有关的)  那么是按照字符数量读取数据
print(f.read(15)) # # 如果超出字符数量 那么会返回所有数据

# 及时关闭
f.close()

f = open('t6.txt',mode='r',encoding='utf-8')
# print(f.readlines()) # 会把每一行数据和换行符进行读取,并且返回一个列表
# print(f.readlines(6)) #  # 比如第一行是9个字符 你如果输入的字符数小于9 那么他是会默认返回整个一行的
print(f.readlines(13)) # 如果读取到第一行的换行符那么他会默认的读取第二行,以此类推




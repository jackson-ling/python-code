# s = '我爱 \npython '   # \n 是一个换行符
# print(s)

# \转义字符 把含有特殊含义的字符转换成普通字符
s = '我爱 \\npython '
print(s)

# 原生字符
s = r'我爱 \npython'
print(s)

# 在你们后面针对路径保存文件的时候 一定要带上转义字符 防止路径的报错
s1 = 'D:\qd\np'
print(s1)

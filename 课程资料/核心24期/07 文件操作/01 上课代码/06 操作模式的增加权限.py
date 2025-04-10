"""w+"""
# f = open(file='t9.txt',mode='w+',encoding='utf-8')   # 文件不存在会被创建
# # f.write('125')
# f.write('256') # 覆盖写入  # 默认光标会在最后
#
# f.seek(0) # 需要先把光标移动到最前面在读
# print(f.read())

"""r+"""
# f = open(file='t2.txt', mode='r+',encoding='utf-8') # 文件不存在会报错
# #
# f.write('125')# 按照字符数覆盖写入(受光标位置的影响)
# f.seek(0)  # 需要先把光标移动到最前面在读
#
# print(f.read())


"""a+"""
f = open(file='k8.txt',mode='a+',encoding='utf-8') # 文件不存在会被创建
# f.write('256')
f.write('6666') # 在a或a+模式 都是代表追加写入  而不是覆盖
f.seek(0) # 在后面 与文件里面有数据 但是读取为空 考虑一下光标的影响
print(f.read())

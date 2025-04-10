arr = ['1', '2', 3, 4, 5, '6', '7']

"""
请将 arr 里面的每一个数据进行数值+1的操作，再保存到txt文件里面

文件名为: hello.txt
文件内容: 2,3,4,5,6,7,8
"""

# 先转型
# map(func,序列)
result = map(lambda x:int(x) + 1,arr)
# print(result)
# print(list(result))

# 字符串的join方法进行对序列的重新组合
content = ','.join([str(i) for i in result])
print(content)
print(type(content))

# 数据保存
with open('hello.txt',mode='w',encoding='utf-8') as f:
    # 字符串和二进制
    f.write(content)











arr = ['1', '2', 3, 4, 5, '6', '7']

"""
请将 arr 里面的每一个数据进行数值+1的操作，再保存到txt文件里面

文件名为: hello.txt
文件内容: 2,3,4,5,6,7,8 
"""
# 第一步 将列表里面的每一个元素变成数值类型然后再相加
# map 它是会默认把序列的每一个元素进行便利的
# map(函数名,序列)
def func(x):
    # print(x)
    # print(x,type(x))
    s = int(x) + 1  # 将数据进行强转为int   进行数值+1
    return s # 将函数内部的数据返回到函数外部 实现内外的数据共享
result = map(func,arr)
# res = list(result)

# join 可以将一个序列合并成新的字符串
# join是字符串的方法 列表里面的元素必须都是字符串

#
# content = ','.join(res) # 括号里面是需要传递一个序列的
# print(content)

# 需要将列表的int数据再一次强转为str类型
# 列表推导式
content1 = ','.join([str(i) for i in result])
print(type(content1))

# 将数据保存到文件里面去
with open(file='hello.txt',mode='w',encoding='utf-8') as f:
    # 只能写入字符串和二进制
    f.write(content1)

# 根据不同的数据类型是有不同的方法操作的



int_to_char = "0123456789ABCDEF"  # 把所有的情况列出
char_to_int = {}

for idx, chr in enumerate(int_to_char):
    char_to_int[chr] = idx  # 逐个遍历字符，让被遍历的字符作为键，值是 idx
    print(chr,idx)
'''
知识点遗漏：给字典赋值
字典[键]=值
'''


# k进制数字x转成10进制
def K_To_Ten(k, x):
    ans = 0
    x = str(x)  # 确保输入是字符串类型
    x = x[::-1]  # 反转字符串，从低位到高位计算
    for i in range(len(x)):
        ans = ans + char_to_int[x[i]] * k ** i  # 用键访问值，前面已经做好了匹配
    return ans

print(K_To_Ten(2, 1101101))  # 这里传入的是整数，但函数内部会将其转换为字符串进行处理

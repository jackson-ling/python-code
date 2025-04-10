int_to_char = "0123456789ABCDEF"  # 把所有的情况列出
char_to_int = {}

for idx, chr in enumerate(int_to_char):
    char_to_int[chr] = idx  # 逐个遍历字符，让被遍历的字符作为键，值是 idx

'''
知识点遗漏：给字典赋值
字典[键]=值
'''

#十进制转任意进制
def Ten_to_K(k,x):
    ans=""
    while x!=0:
        ans+=int_to_char[x%k] #16进制的余数可能大于10，这个时候就要查找对应的16进制值
        x//=k  #得到除2之后的结果，方便再次用它除2求余数
    return ans[::-1]

print(Ten_to_K(2,19))
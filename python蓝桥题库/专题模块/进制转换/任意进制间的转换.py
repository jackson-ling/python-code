#原理，以10进制作为桥梁

# 例如 N 进制 转 M 进制

#预备内容
int_to_char = "0123456789ABCDEF"  # 把所有的情况列出
char_to_int = {}

for idx, chr in enumerate(int_to_char):
    char_to_int[chr] = idx  # 逐个遍历字符，让被遍历的字符作为键，值是 idx

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

#十进制转任意进制
def Ten_to_K(k,x):
    ans=""
    while x!=0:
        ans+=int_to_char[x%k] #16进制的余数可能大于10，这个时候就要查找对应的16进制值
        x//=k  #得到除2之后的结果，方便再次用它除2求余数
    return ans[::-1]

N,M=map(int,input().split())
x=input()
y=K_To_Ten(N,x)
z=Ten_to_K(M,y)
print(z)
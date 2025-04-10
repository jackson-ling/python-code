int_to_char="0123456789ABCDEF"
char_to_int={}

for idx,chr in enumerate(int_to_char):
    char_to_int[chr]=idx

def k_to_ten(k,x):
    ans=0
    x=str(x)
    x=x[::-1]
    for i in range(len(x)):
        ans+=char_to_int[x[i]]*k**i
    return ans

def ten_to_k(k,x):
    ans=''
    while x!=0:
        ans+=int_to_char[x%k]
        x//=k
    return ans[::-1]

T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    s = input().strip() # 去除头尾的空白字符和换行符（输入的时候回车残生了\n）
    a=k_to_ten(N,s)
    b=ten_to_k(M,a)
    print(b)

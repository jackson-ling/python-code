int_to_char="123456789ABCDEF"
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
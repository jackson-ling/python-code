# 输入一个正整数n表示需要配置的题目量
n=int(input())
# 自己电脑每题5分钟；洛谷每题3分钟，还要多花11分钟
# 本地短输出Local，否则Luogu
a=5*n
b=3*n+11

if a<b:
    print('Local')
elif a==b:
    pass
elif a>b:
    print('Luogu')
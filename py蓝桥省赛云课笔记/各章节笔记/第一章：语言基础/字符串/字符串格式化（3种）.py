#format(用{}占位)
a=1
b=2
c=3
print("你{}我{}他{}".format(a,b,c))#注意是  ‘’.‘’

#f
a=1
b=2
c=3
print(f'你{a}我{b}他{c}')

#保留小数的操作(格式：{变量：保留小数点})
a=1.35
b=2.65
print(f'a={a:.1f}   b={b:.1f}')

#%s
a=1
b=2
c=3
print("a=%s b=%s c=%s"%(a,b,c))
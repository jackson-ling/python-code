# 目标是判断识别码，就把这个单独分离出来
isbn=input()   #注意数据类型是字符串,
               #在涉及数值计算时注意数据的类型
qm=isbn[0:11].replace('-','')#提取数字，替换字符’_‘
hm=isbn[12]    #提取识别码

total=0
for i in range(0,9):
    total+=(i+1)*int(qm[i])   #输入的数据类型是任意的，存储在列表中，注意强转数据类型
vc=total % 11#按要求提取符合识别码的要求
if vc==10:
    vc='X'

if str(vc)==hm: #1.注意强转类型，hm是字符串  2.判断是否相等，完成题目要求
    print('Right')
else:
   print(isbn[0:12]+str(vc))    #运用字符串的拼接，注意类型转换



# 方法二：
s=input()
tot=0
cnt=1#按照标识码的计算规则，第一位乘1以此类推，先初始化，后面可以运用循环或者自增cnt的值 来计算tot
for i in range(len(s)-1):
    if s[i]!='-':
        tot+=int(s[i])*cnt
        cnt+=1
m=tot%11
if m<10:
    c=m
else:
    c='X'

if [-1]==str(c):#input()类型是字符串。要对c强转乘字符串类型
    print('Right')
else:
    print(s[:-1]+str(c))
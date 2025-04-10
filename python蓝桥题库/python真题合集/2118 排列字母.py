li=['A','B''C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
li1=[]
a=input()
for i in li:
    for j in a:
        if str(j)==str(i):
            li1.append(j)
        else:
            continue
for i in li1:
    print(i,end='')

#其他优秀解法
# 同样又是字符串的考点，脑子里只有列表
# （sort（）函数的妙用，是我没想到的）

# 方法一：
print(''.join(sorted(input())))

#方法二：
b = "WHERETHEREISAWILLTHEREISAWAY"
c = []
for i in b:#对比我的方法，遍历字符串就比在列表中一个个敲效率高太多了
    c.append(i)
c.sort()
for i in c:
    print(i, end="")
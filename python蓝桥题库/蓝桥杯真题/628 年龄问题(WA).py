#本题完全没思路，看了题解也是懵的

'''
题目：
s夫人说20年前它丈夫的年龄是她的2倍，
而现在他的年龄是我的1.5倍，求s夫人的年龄
'''


for i in range(20,101):#不知道夫人的年龄因此去遍历，20年前不可能小于0岁，20开始，常理到100岁是合理的
    a=(i-20)*2
    if a+20==1.5*i:
        print(i)
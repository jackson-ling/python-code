# 输入七行表示周一到周日的安排，每行两个数，一个是学校上课时间，一个妈妈安排的上课时间
# 要求：每天超过八小时会不高兴，高兴不会持续到第二天，问下周哪天  最 不高兴

# 方法一：运用列表
ls1=[]#用列表来收集每一天的总时间
maxx=0#最愤怒的时间，初始化为0
maxi=0#最愤怒的那天是星期几，初始化为0
for i in range(1,8):
    ls=[int(i) for i in input().split()]#创建列表来收集学校上课时间和妈妈安排的上课时间
    tot=ls[0]+ls[1]#计算总时间
    ls1.append(tot)#把数据添加到列表
for i in range(len(ls1)):
    if ls1[i]>8 and ls1[i]>maxx:#先初始化maxx，通过遍历,每一次去比较最大愤怒时间，只要符合条件就重新赋值
        maxx=ls1[i]
        maxi=i #把最大愤怒时间重新赋值后，记录下今天是周几
if maxx==0:
   print(0)
else:
    print(maxi+1)


# 方法二:运用字典
dic={}
for i in range(1,8):#要用字典来对应取值，先去遍历每一天，之后对应时长
    sch,ex=map(int,input().split())#接受输入的两个时长
    dic[i]=(sch,ex)#对字典的键和值进行定义，进而对应每一天的时长
max_anger=0
flag_day=0
for day,val in dic.items():
    if val[0]+val[1]>8 and val[0]+val[1]>max_anger:
        max_anger=val[0]+val[1]#通过遍历操作，每一次都和条件对比，之后对最愤怒的时长重新赋值
        flag_day=day
print( flag_day)
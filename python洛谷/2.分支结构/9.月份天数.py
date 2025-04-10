y,m=map(int,input().split())
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    print(31)
elif m==4 or m==6 or m==9 or m==11:
    print(30)
elif (y%4==0 and y%100!=0) or y%400==0:
    #注意这里分普通闰年和实际闰年，是选择关系不是两个都要满足
     if m==2:
        print(29)
elif (y%4!=0 and y%100==0) or y%400!=0:
    if m==2:
        print(28)
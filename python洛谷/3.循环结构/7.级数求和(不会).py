k=int(input())
tot=0
n=1
while True:
    if tot>k:
        break
    tot+=1/n
    n+=1
print(n-1)#n有起始值1，那么循环次数也是n的值，这个值才是我么要的，最后要减去起始值1
# （不懂就假设k=2，按照程序运行去写值的变化）

#因为是n一直在增加，具体的范围不确定，用死循环
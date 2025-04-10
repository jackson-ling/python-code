import datetime
T=int(input())
start=datetime.datetime(1970,1,1,0,0,0)
for i in range(0,T):
    a=input().split()  # 注意：分割后返回的列表类型
    x=int(a[2])  # 每过x分钟就会响一次铃声，这里转换类型，后续在timedelta中使用

    # 注意这里的字符串格式，和前面的字符窜是一一对应的
    time=datetime.datetime.strptime(a[0]+a[1],"%Y-%m-%d%H:%M:%S")

    deltatime=time-start

    n=deltatime//datetime.timedelta(minutes=x)

    # 易错：注意题目最后输出的是字符串，还需要再强转一次
    end=(start+n*datetime.timedelta(minutes=x)).strftime("%Y-%m-%d %H:%M:%S")

    print(end)


for k in range(3):
 for i in range(10):
        print(i)
        if i == 5:
            continue     # 在循环任务中, 一旦遇到了 continue 关键字, 那么就会退出当前的这一次循环任务,对后面的循环是没有任何的影响的
                      # 在嵌套循环中 continue 作用域距离最近的循环任务, 满足就近原则
        print(i)
for k in range(3): # 012
    for i in range(0,10):
        print(i)
        if i == 4:
            break   # 在循环任务中, 一旦遇到了 break 关键字, 那么就会终止当前的循环任务(后面直接不执行)
                    #  在嵌套循环中 break 作用域距离最近的循环任务, 满足就近原则
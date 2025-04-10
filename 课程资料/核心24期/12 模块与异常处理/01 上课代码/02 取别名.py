# 需求： 运行后暂停2秒打印hello
"""
1. 导入time模块或导入time模块的sleep功能 (睡眠功能)
2. 调用功能
3. 打印hello
"""

# import 模块名 as 别名
import time,random1
# # time.sleep(2) # 睡眠2 默认单位s
# # print('hello')
#
# 实现随机的睡眠 random
# time.time() 表示记录当前的时间
start = time.time() # 记录开始的时间
time.sleep(random.randint(2,5)) # 表示随机睡眠2到5s
print(time.time() - start) # 打印花费的时间
print('hello')

# import time as ti  对模块名取一个别名
# ti.sleep(2)
# print('hello')

# 对功能名取一个别名
# from time import sleep as sl
# sl(2)
# print('hello')


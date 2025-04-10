"""正左直角三角形
*
**
***
****
*****
"""

# print('-------------正左三角形--------------')
# for i in range(1,6):# 12345 外层循环控制行数
#     # print(i)
#     for k in range(i): # i= 1
#         print('*',end='')
#     print()


"""
要打印的效果:正右三角形
    * 4
   **3
  ***2
 ****1
*****0
"""

for i in range(1,6):# 12345 外层循环控制行数
   # 先打印空格
   span = 5 - i
   for k in range(span):
       print(' ',end='')
   # 打印星星的数量
   for e in range(i):
       print('*',end='')

   print()



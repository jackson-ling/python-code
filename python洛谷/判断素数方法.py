'''方法一'''
for i in range(2,12): # 外层循环是选择2到100数
    for j in range(2,i):
        if i % j == 0: # 那么就表示他有其他的因数  就表示他不是一个素数
            break # 终止最近循环
    else:# 打印素数   如果break没有被执行 那么else就会被执行
        print(i)


'''方法二'''
# # 定义一个函数判断素数
# def is_prime(n):
#     if n==1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True

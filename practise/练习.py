# #
# # # 检测点报错（细节：前提不是三角形的条件可能处在等于的情况，即两边之长小于  等于  第三边长）
# # # list=[int(i) for i in input().split()]
# # # list.sort()
# # # a=list[0]
# # # b=list[1]
# # # c=list[2]
# # # if  a+b<=c or a+c<=b or b+c<=a:
# # #     print('Not triangle')
# # # if a+b>c and a+c>b and b+c>a:
# # #     if a**2 + b**2== c**2:
# # #      print('Right triangle')
# # #     if a**2 + b**2 > c**2:
# # #      print('Acute triangle')
# # #     if a**2 + b**2 < c**2:
# # #      print('Obtuse triangle')
# # #     if a == b or a == c or b == c:
# # #      print('Isosceles triangle')
# # #     if a == b == c:
# # #      print('Equilateral triangle')
# #
# # # x,n=[int(i) for i in input().split()]
# # # for i in range(1,n+1):
# # #     print(x)
# #
# # L=int(input())
# # li1=[]
# # li2=[]
# # tot=0
# # #判断素数
# # for i in range(2,L+1): # 外层循环是选择2到100数
# #     for j in range(2,i):
# #         if i % j == 0: # 那么就表示他有其他的因数  就表示他不是一个素数
# #             break # 终止最近循环
# #     else:
# #         li1.append(i)#列表一都是素数
# #
# # for i in li1:
# #     if tot<=L :
# #      li2.append(i)
# #     else:
# #         pass
# #     tot =sum(li2)
# # for i in li2:
# #  print(i)
# # print(len(li2))
# #
# # print(1,end='')
# # print('\n')
# # print(2)
#
#
# n=int(input())
# def is_prime(n):
#     if n==1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     else:
#         return True
# for i in range(2,n+1):
#     if n%i==0:#重点：如果能被n整除，说明i是n的一个因数
#         if is_prime(i) and is_prime(n//i):
#             #重点：i是从小到大开始遍历的，那么求出来的一定是最大的因数
#             print(n//i)
#             break
#






# n=int(input())
# def is_prime_v2(x):
#     if x==2:
#         return  True
#         #2是质数，不进入下面的判断
#     if x%2==0:
#         #除2以外的偶数都是合数，因为起码有2一个因子
#         return False
#     for num in range(3,int(x**0.5)+1,2):
#         '''
#         起点从3开始，因为上面判断2了，重点判断到跟好x即可，因为在跟好x找到一个银子，
#         那么余数必定在根号x之后，那么这一对就是相同的，没必要重复找
#         step是2是因为上面已经排除偶数了，这里再加进来就会影响电脑性能
#         '''
#
#         if x%num==0:
#             return False
#         else:
#           return True
#

# for i in range(2,n+1):
#     if n%i==0:#重点：如果能被n整除，说明i是n的一个因数
#         if is_prime_v2(i) and is_prime_v2(n//i):
#             #重点：i是从小到大开始遍历的，那么求出来的一定是最大的因数
#             print(n//i)
#             break


# li=[int(i) for i in input().split()]
# print(li)

a=input()
print(a)
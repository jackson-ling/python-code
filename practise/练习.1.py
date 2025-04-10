# # def is_prime_v2(x):
# #     if x==2:
# #         return  True
# #         #2是质数，不进入下面的判断
# #     if x%2==0:
# #         #除2以外的偶数都是合数，因为起码有2一个因子
# #         return False
# #     for num in range(3,int(x**0.5)+1,2):
# #         '''
# #         起点从3开始，因为上面判断2了，重点判断到跟好x即可，因为在跟好x找到一个银子，
# #         那么余数必定在根号x之后，那么这一对就是相同的，没必要重复找
# #         step是2是因为上面已经排除偶数了，这里再加进来就会影响电脑性能
# #         '''
# #
# #         if x%num==0:
# #             return False
# #
# # print(is_prime_v2(3))
# #
# def is_prime(x):
#     if x==1:
#         return False
#     for i in range(2,int(x**0.5)+1):
#         if x%i==0:
#             return False
#     return True
# print(is_prime(3))
# l=int(input())
# a=[1 for i in range(l+1)]#生成一个每个数据都一样的列表，1循环l+1次
# print(a)
# print("hello"+"nihao")

li1=[i for i in input()]
li2=[i for i in input()]
for i in li1:
    for j in li2:
        if j in li1:
            li1.remove(j)
for i in li1:
    print(i,end='')
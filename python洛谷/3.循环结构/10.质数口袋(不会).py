L= int(input())
prime_package=[]

def is_prime_v2(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True

#易错点：最后return True语句要和for循环语句同级，不能放在if语句里面

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
#     else:
#         return True


for num in range(2,L+1):
    if is_prime_v2(num) and sum(prime_package)+ num <= L:
        prime_package.append(num)
    if sum(prime_package)+num >L:
         break


for prime in prime_package:
    print(prime)

print(len(prime_package))



# L=int(input())
# li1=[]
# li2=[]
# tot=0
# #判断素数
# for i in range(2,L+1): # 外层循环是选择2到100数
#     for j in range(2,i):
#         if i % j == 0: # 那么就表示他有其他的因数  就表示他不是一个素数
#             break # 终止最近循环
#     else:
#         li1.append(i)#列表一都是素数
#
# for i in li1:
#     if tot<L :
#      li2.append(i)
#     else:
#         pass
#     tot += i
# for i in li2:
#  print(i)
# print(len(li2))




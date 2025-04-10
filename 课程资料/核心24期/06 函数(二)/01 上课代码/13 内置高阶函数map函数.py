# map(func, lst)，将传入的函数变量func作用到lst变量的每个元素中，并将结果组成新的列表(Python2)/迭代器(Python3)返回。
# map(函数名,序列)

list1 = [1,2,3,4,5]
def fun(x):
      print(x)
      return x + 5

# # 默认返回的是对象
result = map(fun,list1)# 会默认遍历列表的每一个元素   并且把元素传递函数的形式参数接受
print(result)
print(list(result)) # 通过list强转看对象里面的具体内容

# lambda简化我的函数逻辑
# # lambda只能去代替函数逻辑
# result1 = map(lambda x:x + 5,list1)
# print(list(result1))
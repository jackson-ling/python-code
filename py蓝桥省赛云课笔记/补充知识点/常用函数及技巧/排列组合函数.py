'''
说明：调用函数都是过程，需要强转成列表查看结果或者用循环遍历，返回的是元组

import itertools

1.排列函数（考虑顺序）
print(list(permutations(可迭代的对象，排列对象的个数)))


2.组合函数（不考虑顺序）
print(list(combinations(可迭代的对象，排列对象的个数)))





例子：

import itertools
a=[1,2,3,4]

b=itertools.permutations(a,3)
for i in b:
 print(i)

c=itertools.combinations(a,2)
for i in c:
 print(i)




(1, 2, 3)
(1, 2, 4)
(1, 3, 2)
(1, 3, 4)
(1, 4, 2)
(1, 4, 3)
(2, 1, 3)
(2, 1, 4)
(2, 3, 1)
(2, 3, 4)
(2, 4, 1)
(2, 4, 3)
(3, 1, 2)
(3, 1, 4)
(3, 2, 1)
(3, 2, 4)
(3, 4, 1)
(3, 4, 2)
(4, 1, 2)
(4, 1, 3)
(4, 2, 1)
(4, 2, 3)
(4, 3, 1)
(4, 3, 2)
(1, 2)
(1, 3)
(1, 4)
(2, 3)
(2, 4)
(3, 4)


'''
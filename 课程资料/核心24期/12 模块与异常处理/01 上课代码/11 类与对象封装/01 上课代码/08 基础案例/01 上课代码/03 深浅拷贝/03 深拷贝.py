# 深拷贝 拷贝对象及其子对象

import copy


# deepcopy 深拷贝: 把对象里面的内容全部赋值一份(适用于所有维度的数据)
a = [1,2,[1,2,3],3,4,5]
b = copy.deepcopy(a) #是我们的深拷贝

a[2][1] = 5
print(id(a))
print(id(b))

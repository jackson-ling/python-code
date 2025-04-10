import copy
# deepcopy 深拷贝: 把对象里面的内容全部赋值一份(适用于所有维度的数据)
a1 = [1,3,[1,4,5]]
b = copy.deepcopy(a1)  # 利用深拷贝去拷贝多维对象
a1[2][0] = 25
print(a1)
print(b)
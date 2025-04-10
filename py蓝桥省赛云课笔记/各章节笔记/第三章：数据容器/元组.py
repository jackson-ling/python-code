#元组和列表大部分方法相同，区别在于元组不可以修改

#元组的特点是由逗号分隔（创建元组需要注意）

#如果需要修改，先转成列表类型再修改

a=['1','2','3']
b=tuple(a)
print(type(a))
print(type(b))

#创建元组
tup=(1,)
tup1=(1)
print(type(tup))  # tuple
print(type(tup1))  # int
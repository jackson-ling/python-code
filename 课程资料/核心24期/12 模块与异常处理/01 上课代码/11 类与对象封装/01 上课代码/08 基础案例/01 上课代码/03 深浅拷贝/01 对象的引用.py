a = [1,2,3,4,5]
b = a
a[0] = 5
print(a)
print(b)
# 如果2个变量引用的同一对象那么id是一样的
print(id(a))
print(id(b))

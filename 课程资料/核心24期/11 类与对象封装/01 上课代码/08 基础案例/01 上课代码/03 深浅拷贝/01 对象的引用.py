a = [1,2,3,4]
b = a
print(a)
print(b)


a[1] = 9
print(a)   # 随着a的改变b也是回受影响的 是因为他们引用的是同一个对象
print(b)

# id地址一样就表示他们引用是同一个对象
print(id(a))
print(id(b))


dict1 = {
    'name':'泽言',
    'age':25,
    '职业':'python讲师'
}

a = dict1.get('kk')  #   空类型  代表无类型, 无结果的对象 理解为一个空的容器
print(type(a))

print(bool(a)) # #他的布尔类型是False
# None可以作为临时的判断条件
if not a :      #  只有if 后面的的条件布尔值为True 它才会被执行
    print('泽言')

dict1 = {
    'name':'泽言',
    'age':25,
    '职业':'python讲师'
}

# # 他返回的是一个一个键
# for i in dict1:
#     print(i)


# # 他返回的是一个一个键
# # 去遍历字典本身的方法
# for i in dict1.keys():
#     print(i)


# 他返回的是一个一个值
# for i in dict1.values():
#     print(i)

# 返回键和值  返回的是元组类型(固定返回,已经写好的底层代码)
for i in dict1.items():
    print(i)

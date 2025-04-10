# 定义字典
d = {'a': 10, 'b': 20, 'c': 10, 'd': 30}

# 目标值
target = 10

# 遍历字典，查找目标值对应的键
for key, value in d.items():
    if value == target:
        print(key,value)


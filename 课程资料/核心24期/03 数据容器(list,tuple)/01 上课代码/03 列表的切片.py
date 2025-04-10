# `[起始值:结束值:步长]` range很相似
#
# - start:  起始索引，从0开始，-1表示结束
# - stop：结束索引
# - step：步长，end-start，步长为正时，从左向右取值。步长为负时，反向取值

name_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# 取a到e 步长不写默认为1
# print(name_list[0:5]) #   他是一个左闭右开区间


# # 取全部的数据
# print(name_list[0:7])
# # 如果起始值写了 而我们的结束值没有写  那么他会默认从起始值开始取完
# print(name_list[0:])

# # 要取e之前的所有数据
# print(name_list[0:4])

# # 如果起始值不写 而我们的结束值写了 那么他会默认从头开始取到结束值
# print(name_list[:4])

# 步长参数
# 步长不写默认为1
# 顺序取值  是从左往右  步长一定要为正数(正数步长方向也是 从左往右,负数步长是从右往左)
# print(name_list[0:5])
# print(name_list[0:5:2])
# print(name_list[0:5:-2])  #返回空列表 方向相反

# 步长为负 从右向左取值 0 表示结束索引(由于左闭右开 0是取不到的)
print(name_list[4:0:-1])

# 思考 步长可不可以为0？
# print(name_list[0:4:0])  slice step cannot be zero  #python底层源码自己规定好的 步长不能为0

#第一个方法 换一种容器 字典
# 第二种方法 就是 使用我们待会会讲的index方法
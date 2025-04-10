# """
# 作业2：
# 运行代码之后，请找出下面代码错误并且修正
#
# 提示：深浅拷贝,数据不重复 
# """
#***********************
# 定义了一个字典
import copy
data = {
    'cate': '童书馆',
    'sub_cate': None  # 将字典的 'sub_cate' 赋值成了none
}
# 定义了一个列表 保存了5条数据
sub_cate = ['科普百科', '儿童文学', '幼儿启蒙', '动漫卡通', '少儿英语']


# 定义空的列表
all_cate = []
# 在字典的数据添加 他们引用的同一个对象  字典的键都是相同的
# 会将前面的内容覆盖掉 添加到列表里面去
#
# [{'cate': '童书馆', 'sub_cate': '儿童文学'},{'cate': '童书馆', 'sub_cate': '儿童文学'},]
for cate in sub_cate:
    print(cate)
    data['sub_cate'] = cate # 是将列表里面的每一个数据赋值给字典
    # print(id(data)) # 字典的id是一模一样的,那就说明字典引用的是同一个对象
    # 解决问题的方法
    # 给每一个字典单独去开辟一个对象 让他们的数据互不影响
    # 深浅拷贝
    # 浅拷贝
    # all_cate.append(copy.copy(data))  # 只适用于一维维度
    # print(id(copy.copy(data)))
    # 深拷贝
    all_cate.append(copy.deepcopy(data))
    print(id(copy.deepcopy(data)))   # 适用于所有维度
    # all_cate.append(data)   # 是将字典添加到空的列表里面去

print(all_cate)



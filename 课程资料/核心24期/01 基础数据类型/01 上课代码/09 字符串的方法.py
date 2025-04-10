"""strip()方法"""
# # 默认去掉 string 左右两边的空白字符 去除首尾字符
s = '\n # hello world ! # \n' #\n就是换行符
# print(s)
# # print(s.strip().strip('#'))    # 这里的\n或被strip识别为空白字符
# # print(s.strip().strip('#'))     # 链式调用法   那就需要保证前面调用方法的数据任然是字符串类型
# print(type(s.strip()))
#
# # 如果strip()里面输入的字符不存在,  不会报错,会返回默认字符串
# # print(s.strip('9'))
#
# """replace()方法"""
# # 把 string 中的 old_str 替换成 new_str
# # print(s.replace('#','7'))
# print(type(s.replace('#','7')))
# print(s.replace('#','7').replace('7','9'))  # 链式调用法
#
# # replace()里面输入的字符不存在,不会报错,会返回默认字符串
# print(s.replace('9','s'))


"""split()"""
# 默认以空白字符进行分割
# print(s.split())
# # # 他返回的是一个列表类型  \n他会被当做空白字符  对个连续空白会被识别为1个
# print(s.split('#')) # 我此时能不能像前面一样对它进行链式调用 答案是否定的
# print(type(s.split('#'))) # 列表类型是没有字符串的方法(不同数据类型有自己的方法不能混用)
#
# print(s.split('7')) # 指定一个不存在的   把默认值作为一个列表返回
# # print(s.split('')) # 这个表示空字符 这个方法不支持用空字符分割
# print(s.split(' ')) # 代表空格字符

"""join()方法"""
# 将 seq 中所有的元素（字符串类型）合并为一个新的字符串  seq代表就是序列(str list, set..)
# 数值类型不是序列
# 用列表序列举一个例子
s1 = '张三，李四，王五'
name1 = s1.split('，')
# name= s1.split(' ')
# print(name1,name)
# #
name2 = '_'.join(name1)# 传递一个序列
name2 = ' '.join(name1)
print(name2)













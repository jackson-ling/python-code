# """
# 假设有以下地址:
#
#     https://www.bbsmax.com/A/?user=7001&id=1305
#     https://www.bbsmax.com/A/?user=7002&id=1306
#     https://www.bbsmax.com/A/?user=7003&id=1307
#     https://www.bbsmax.com/A/?user=7004&id=1308
#     https://www.bbsmax.com/A/?user=7005&id=1309
#     https://www.bbsmax.com/A/?user=7006&id=1310
#     https://www.bbsmax.com/A/?user=7007&id=1311
#     https://www.bbsmax.com/A/?user=7008&id=1312
#     https://www.bbsmax.com/A/?user=7009&id=1313
#     https://www.bbsmax.com/A/?user=7010&id=1314
#
# 观察以上地址规律, 将以上规律用循环构建出来

# range(起始值,结束值,步长)   左闭右开
# 构造user的规律
user1 = range(7001,7011) # 左闭右开 步长不写默认为1
# print(user1)
# 构造id的规律
id_1 = range(1305,1315)  # 左闭右开 步长不写默认为1
print(list(user1))
print(list(id_1))

# zip
for use_2 ,id_2 in zip(user1,id_1):
    # print(use_2,id_2)
    print(f'https://www.bbsmax.com/A/?user={use_2}&id={id_2}')

# 方法二
user3 = 7000
id_3 = 1304
for j in range(1,11):
    print(j)
    print(f'https://www.bbsmax.com/A/?user={user3 + j}&id={id_3 + j}')
# 学编程 要去尝试一下新的方法 实践自己的想法 看看一个问题 能不能找到其他的解决思路











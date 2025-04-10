"""
请用列表推导式构建以下地址规律
    https://www.maoyan.com/board/4?offset=0
    https://www.maoyan.com/board/4?offset=10
    https://www.maoyan.com/board/4?offset=20
    https://www.maoyan.com/board/4?offset=30
    https://www.maoyan.com/board/4?offset=40
    https://www.maoyan.com/board/4?offset=50
    https://www.maoyan.com/board/4?offset=60
    https://www.maoyan.com/board/4?offset=70
    https://www.maoyan.com/board/4?offset=80
    https://www.maoyan.com/board/4?offset=90
请在下方编辑代码:

"""
# 规律 每一个网址offset增加10
# 列表推导式可以节省我们的一个代码量
# range是左闭右开区间
res = [f'https://www.maoyan.com/board/4?offset={i}'for i in range(0,91,10)]
# # print(res)
# # 格式化输出
# import pprint
# pprint.pprint(res)

# 把推导式进行拆分
# 第一部分
for i in range(0,91,10):
    # print(i)
    # 第二部分
    print(f'https://www.maoyan.com/board/4?offset={i}')







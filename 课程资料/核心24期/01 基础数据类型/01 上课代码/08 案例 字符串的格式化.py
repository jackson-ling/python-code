"""
    猫眼top100的网址
    第一页：https://maoyan.com/board/4?offset=0
    第二页：https://maoyan.com/board/4?offset=10
    第三页：https://maoyan.com/board/4?offset=20
    ....
    第十页：https://maoyan.com/board/4?offset=90

    请分别使用三种字符串构建的方法创建所有的请求地址
"""
# range('起始值','结束值','步长') 左闭右开区间
for i in range(0,91,10):
    print(f'https://maoyan.com/board/4?offset={i}')
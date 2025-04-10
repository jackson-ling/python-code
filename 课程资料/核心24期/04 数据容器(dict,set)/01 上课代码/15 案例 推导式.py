"""
https://movie.douban.com/top250?start=0&filter=
https://movie.douban.com/top250?start=25&filter=
https://movie.douban.com/top250?start=50&filter=
https://movie.douban.com/top250?start=75&filter=
https://movie.douban.com/top250?start=100&filter=
https://movie.douban.com/top250?start=125&filter=
https://movie.douban.com/top250?start=150&filter=
https://movie.douban.com/top250?start=175&filter=
https://movie.douban.com/top250?start=200&filter=
https://movie.douban.com/top250?start=225&filter=
# """ # 每一个url地址都加了25

# range 函数
# range(起始值,结束值,步长)步长不写默认为一
res1 = [ f'https://movie.douban.com/top250?start={i}&filter='for i in range(0,226,25)]
# print(res1)

# 格式化输出
import pprint
pprint.pprint(res1)


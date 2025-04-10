'''

题目：小蓝家的网络带宽是 200 Mbps，请问使用小蓝家的网络理论上
      每秒钟最多可以从网上下载多少 MB 的内容。

1byte=8bit
1MB=8Mbps
1GB=1024MB

Mb表述的是bits，MB表示的是byte 1byte=8bits


一个字节=八个bit位
1 Byte(B)=8 bits(b)
1 B=8 b
1 KB=2**10 B=1024 B
1 MB=2**10 KB=2**20B
1 CB=2**10 MB=2**20KB=2**30 B
1 TB=2**10 GB=2**20MB=230KB=2**40 B

'''
x=200//8
print(x)
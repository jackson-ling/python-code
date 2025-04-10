import requests
# 图片/视频/音频  都属于二进制数据
response = requests.get('https://img2.baidu.com/it/u=213978626,894923520&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=357')
img_url = response.content # 打印二进制数据
print(img_url)

# 二进制数据不支持编码
with open('feng.jpg',mode='wb') as f:
    f.write(img_url)
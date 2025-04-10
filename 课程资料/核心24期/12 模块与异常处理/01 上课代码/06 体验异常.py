# f = open('你好1.txt', mode='r', encoding='utf-8') # r模式文件不存在的话直接报错不会自动创建

# try:
#     可能发生错误的代码
# except:
#     如果出现异常执行的代码
# 如果出现的异常捕获到了, 那么不会影响后续的代码执行
try:
    f = open('你好1.txt', mode='r', encoding='utf-8')
    # 如果try下面的代码发生报错 走except下面的代码逻辑
except:
    f = open('你好1.txt', mode='w', encoding='utf-8')


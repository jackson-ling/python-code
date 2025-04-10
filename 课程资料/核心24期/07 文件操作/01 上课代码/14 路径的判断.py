import os
print('当前的绝对路径: ',os.path.abspath('.'))  # .表示当前文件路径 绝对路径
print('当前的绝对路径: ',os.path.abspath('..'))  # ..表示上一级文件路径 绝对路径

print(__file__) # 返回的是当前文件绝对路径

print(os.path.basename(__file__))   # 返回是的当前py文件的名字

print(os.path.splitext(__file__))  # 文件路径和尾缀分开， 返回的是一个元组内容  后面用的比较多的

# 固定方法 看一下



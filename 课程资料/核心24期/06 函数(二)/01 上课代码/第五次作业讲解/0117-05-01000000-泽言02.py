"""
定义一个函数, 实现登录的功能

    要求: 现在有用户名(user_name)  密码(password)
    if  else

        如果用户输入正确的用户名和密码, 提示 "登录成功" 退出循环
        如果用户输入错误的用和户名密码, 提示 "用户名或密码输入错误"
        如果用户输入三次错误, 提示 "您输入错误的次数过多,登录异常", 需要进行变量的累加
        (这里需要用一个变量去记录错误的次数)

    提示: 循环  +   逻辑判断
"""
# 循环 函数 判断 是一个综合案例
user_name = 'zeyan'    # 全局变量
password = '123456'

# 你知道自己到底要输入多少次吗?
# 死循序 + break
a = 25  # 全局变量   他可以在任何地方被引用 如果想修改的话 必须使用global进行声明
def login():
    s = 0 # 避免s被重新赋值
    while True:
        user = input('请输入你的用户名:')
        pwd = input('请输入你的密码:')
        # = 只是变量赋值 == 才是条件比较
        if user == user_name and pwd == password: # and表示2个条件都要满足
            print('登录成功')
            # break # 退出死循环  而不是去退出一个函数
            return      # 函数一旦遇到我的return那么整个函数就会停止执行
                        # return 后面什么都不写默认返回的就是none

        else:
            print("用户名或密码输入错误")

            global a
            a += 1
            print(a)
            # 每运行错误一次 就加一
            s += 1
            print('输入错误的次数', s)
            if s >= 3:
                print("您输入错误的次数过多,登录异常")
                break
                # return

# 调用 函数 去执行函数里面的代码逻辑
login()







"""
斐波那契数列（Fibonacci sequence），
又称黄金分割数列，因数学家莱昂纳多·斐波那契（Leonardo Fibonacci）以兔子繁殖为例子而引入，故又称为“兔子数列”，

指的是这样一个数列：1、1、2、3、5、8、13、21、34、……n

在数学上，斐波那契数列以如下被以递推的方法定义：F(0)=0，F(1)=1, F(n)=F(n - 1)+F(n - 2)（n ≥ 2，n ∈ N*）

#自己本身的值是等于前和2个值之 这个就是他的规律  我们写代码 就是在根据规律去写
"""
# 需求第6个斐波那契数
def fib(num): # num是表示第几个斐波拉切数
    if num==1 or num==2:  #
        return 1  # 为了不让他一直循环 设置一个出口 return就会结束掉整个函数  还要去返回一个1  break是不行的
    else:
        result = fib(num - 1) + fib(num - 2)   #函数名+() 代表调用函数
        # num = 6  result = fib(5) + fib(4)   #  单独执行result = fib(num - 1) + fib(num - 2)
        # result = fib(4) +fib(3) + fib(3) + fib(2)
        # result = fib(3) + fib(2) + fib(2) + fib(1) + fib(2) + fib(1) + fib(2)
        # result = fib(2) + fib(1) + fib(2) + fib(2) + fib(1) + fib(2) + fib(1) + fib(2)
        # result = 8

        return result # 每一次去运行函数都会得到一个result返回值 所以是需要写这个return
# 调用函数
print(fib(8))


# break是跳出死循环  是while True搭配的
# return是和函数搭配





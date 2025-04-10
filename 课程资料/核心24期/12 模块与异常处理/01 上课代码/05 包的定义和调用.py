# 方法一 通过 import 调用
# import 包名.模块名.方法

# random os 都是存在于我们这个解释器里面(解释器可以理解为一个包)
import page.q1_word
import page.q2_word


print(page.q1_word.func1(5,9))
print(page.q2_word.func2(51,9))


# 包的作用 就是对不同功能模块进行分类 让它可以快速的调用和区别


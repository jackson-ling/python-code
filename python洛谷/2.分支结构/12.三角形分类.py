#输入三个数abc表示三角形长度，判断能否构成三角形

# 如果三条线段不能组成一个三角形，输出Not triangle
# 如果是直角三角形，输出Right triangle
# 如果是锐角三角形，输出Acute triangle
# 如果是钝角三角形，输出Obtuse triangle
# 如果是等腰三角形，输出Isosceles triangle
# 如果是等边三角形，输出Equilateral triangle

# 如果这个三角形符合以上多个条件，请按以上顺序分别输出，并用换行符隔开

# 当两短边的平方和大于一长边的平方，说明是锐角三角形
# 当两短边的平方和等于一长边的平方，说明是直角三角形
# 当两短边的平方和小于一长边的平方，说明是钝角三角形


# 易错点：能判断是什么类型的三角形  前提  是能构成一个三角形
# 三边关系强调任意
#不能构成三角形两边之和小于   等于    第三边（注意是等于）


list=[int(i) for i in input().split()]
list.sort()
a=list[0]
b=list[1]
c=list[2]
if a+b>c and a+c>b and b+c>a:#前提是一个三角形
    # 默认以输出后换行，不需要像C语言那样需要添加换行符
    if a**2 + b**2== c**2:
     print('Right triangle')
    if a**2 + b**2 > c**2:
     print('Acute triangle')
    if a**2 + b**2 < c**2:
     print('Obtuse triangle')
    if a == b or a == c or b == c:
     print('Isosceles triangle')
    if a == b == c:
     print('Equilateral triangle')
else:
    print('Not triangle')
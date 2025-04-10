# 易错点：要约分，这里用一个求最大公约数函数math.gcd（a，b）

import math
list=[int(i) for i in input().split()]
list.sort()
a=list[0]
b=list[1]
c=list[2]
a1=int(a/math.gcd(a,c))
a2=int(c/math.gcd(a,c))
print(f'{a1}/{a2}')

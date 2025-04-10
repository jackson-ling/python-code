#本题的核心是统计数字的长度
L=0
for i in range(1,2021):
  l=len(str(i))
  L+=l
print(L)
a=[]
for A in range(100):
  for B in range(100):
    for C in range(100):
      if 3*A+7*B+C==315 and 4*A+10*B+C==420:
        a.append(A+B+C)
        break
print(a[0])

#本题需要学习的点：1.遍历范围会不会超时，如何打印最后的结果
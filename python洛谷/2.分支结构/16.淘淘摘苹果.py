#输入10个100-200（包含100，200）的数表示苹果离地面的高度
list=[int(i) for i in input().split()]
#输入一个100-200（包含100，200）的数表示伸直手达到的最大高度，还有一个30厘米的高的凳子
a=int(input())
b=0
for i in list:
  if a+30<i:
      pass
  elif a>=i :
      b+=1
  elif a+30>=i:
      b+=1
print(b)
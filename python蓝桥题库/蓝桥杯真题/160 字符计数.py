#注意in运算符的使用

tot=0
cnt=0
n=input()
li=['a','e','i','o','u']
for i in n:
  if i in li:
      cnt+=1
  else:
      tot+=1

print(cnt)
print(tot)
a=int(input())
if a<=150:
   b=a*0.4463
elif  151<a<400:
    b = 150*0.4463+(a-150)*0.4663
elif a>=401:
    b= 150*0.4463+250*0.4663+(a-400)*0.5663
print('%.1f'% b)

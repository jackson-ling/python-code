a = int(input())
n = int(input())

if a + n >= 8:
    if (a + n) % 7 == 0:  # n=0的情况
        print(7)
    else:
        print((a + n) % 7)

elif a + n <= 7:
    print(a + n)

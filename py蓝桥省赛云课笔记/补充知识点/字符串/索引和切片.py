#正序和逆序，正序的起始索引是0，逆序的起始索引是-1

#正序
word = 'Python'
print(word[3])		# h
'''
关系：当下表索引为n时，表示第n+1个元素（第一个元素的索引下表是0）
'''
#逆序
word = 'Python'
print(word[-3])     # h


#切片（特别注意：区间是左闭右开型）
'''

1.步长可正可负
2.步长为负时，左区间值比右区间值大

'''
word = 'Python'

print(word[0:2])		# Py
print(word[:2])			# Py
print(word[::2])		# Pto
print(word[2:5:])		# tho
print(word[5:2:-1])		# noh
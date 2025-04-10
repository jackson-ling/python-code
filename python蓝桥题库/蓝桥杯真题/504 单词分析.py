#本题思路很巧，好好琢磨

from collections import Counter

a = input()
tot = Counter(a)

# 获取最大出现次数
max_count = max(tot.values())

# 筛选出所有出现次数等于最大次数的字母
max_letters = [key for key, value in tot.items() if value == max_count]

# 输出字典序最小的字母
print(min(max_letters))

# 输出最大出现次数
print(max_count)

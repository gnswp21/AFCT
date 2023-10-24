from collections import defaultdict

n = input()
s = input()

dict = defaultdict(int)
for char in s:
    dict[char] += 1
for char in dict.keys():
    dict[char] %= 1000000007
ans = 1
for val in ["A", "G", "C", "T"]:
    ans *= dict[val]
print(ans % 1000000007)



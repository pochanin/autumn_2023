M = ['abab', 'xx', 'aaaaaa', 'abcbab']
sorted_M = sorted(M, key=lambda x: (-len(set(x)), x))
print(sorted_M)


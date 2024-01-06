num = int(input())
words = input().split()

print(len(set(frozenset(word) for word in words)))

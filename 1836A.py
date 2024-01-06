from collections import Counter

for _ in range(int(input())):
    _ = int(input())
    c = Counter(map(int, input().split()))
    print("no" if any(c[i] > c[i - 1] for i in range(1, 101)) else "yes")

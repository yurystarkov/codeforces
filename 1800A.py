from itertools import groupby

for _ in range(int(input())):
    _ = int(input())
    sound = ''.join([letter for letter, _ in groupby(input().lower())])
    print("YES" if sound == "meow" else "NO")

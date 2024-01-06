from collections import Counter

turns = int(input())
wins_count = Counter(input())

print(
    "Anton"
    if wins_count["A"] > wins_count["D"]
    else "Danik" if wins_count["D"] > wins_count["A"]
    else "Friendship"
)

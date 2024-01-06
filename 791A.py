leemak, bob = map(int, input().split())
years = 0

while leemak <= bob:
    leemak *= 3
    bob *= 2
    years += 1

print(years)

tasks = [list(map(int, input().split())) for _ in range(int(input()))]

print(sum((sum(task) > 1 for task in tasks)))

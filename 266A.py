stones_num = int(input())
colors = input()

remove_num = sum(
    colors[i-1] == colors[i]
    for i in range(1, stones_num)
)

print(remove_num)

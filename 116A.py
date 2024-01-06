stops_num = int(input())

peoples_nums = [0]

for _ in range(stops_num):
    a, b = map(int, input().split())
    peoples_nums.append(peoples_nums[-1] - a + b)

print(max(peoples_nums, default=0))

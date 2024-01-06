input_size = int(input())

for _ in range(input_size):
    peoples_amount, steps_amount, steps_dist, vlad_height = map(int, input().split())
    peoples_heights = [int(h) for h in input().split()]

    companions_amount = sum(
        1 for height in peoples_heights
        if height % steps_dist == vlad_height % steps_dist
        and 0 < abs(vlad_height - height) <= (steps_amount - 1) * steps_dist
    )

    print(companions_amount)

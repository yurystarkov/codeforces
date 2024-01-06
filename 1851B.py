input_size = int(input())

for _ in range(input_size):
    xs_len = int(input())
    xs = [int(x) for x in input().split()]

    xs_sorted = sorted(xs)

    print(
        "NO"
        if any(
            xs[i] % 2 != xs_sorted[i] % 2
            for i in range(xs_len)
        )
        else "YES"
    )

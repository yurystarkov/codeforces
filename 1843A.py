for _ in range(int(input())):
    n = int(input())
    xs = sorted(map(int, input().split()))
    print(0 if n == 1 else sum(xs[-i - 1] - xs[i] for i in range(n // 2)))

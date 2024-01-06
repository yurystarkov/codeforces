for _ in range(int(input())):
    n, m = map(int, input().split())
    x = sum(map(int, input().split()))
    y = sum(map(int, input().split()))

    print("Tsondu" if x > y else "Draw" if x == y else "Tenzing")

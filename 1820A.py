for _ in range(int(input())):
    s = input()
    print(
        1 if s == "^"
        else s.startswith("_") + s.endswith("_") + sum(
            s[i] == s[i - 1] == "_" for i in range(1, len(s))
        )
    )

lines = [input(), input(), input()]

vowels = {'a', 'e', 'i', 'o', 'u'}

is_haiku = (5, 7, 5) == tuple(
    sum(char in vowels for char in line) for line in lines
)

print("YES" if is_haiku else "NO")

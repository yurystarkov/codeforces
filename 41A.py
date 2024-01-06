word, drow = input(), input()

print(
    "YES"
    if ''.join(reversed(word)) == drow
    else "NO"
)

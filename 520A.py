from string import ascii_lowercase

_, word = input(), input()

print("YES" if len(set(word.lower())) == len(ascii_lowercase) else "NO")

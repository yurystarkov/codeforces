from string import ascii_uppercase, ascii_lowercase

word: str = input()

more_uppercase = sum(
    letter in ascii_lowercase
    for letter in word
) < sum(
    letter in ascii_uppercase
    for letter in word
)

print(
    word.upper()
    if more_uppercase
    else word.lower()
)

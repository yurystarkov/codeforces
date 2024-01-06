num = input()

almost_happy = sum(
    digit == "4" or digit == "7" for digit in num
)

print(
    "YES"
    if almost_happy == 4 or almost_happy == 7
    else "NO"
)

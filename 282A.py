x = 0

for _ in range(int(input())):
    sentence = input()

    if "++" in sentence:
        x += 1
    else:
        x -= 1

print(x)

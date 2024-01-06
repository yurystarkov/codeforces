for _ in range(int(input())):
    word = input()

    print(word[0] + str(len(word[1:-1])) + word[-1] if len(word) > 10 else word)

_, answers = input(), input()

print("HARD" if any(answer == "1" for answer in answers) else "EASY")

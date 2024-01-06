num = int(input())

emotions = ["I love" if i % 2 == 0 else "I hate" for i in range(1, num+1)]

print(" that ".join(emotions) + " it")

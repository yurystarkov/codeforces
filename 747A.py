from collections import Counter

length, gene = int(input()), input()

nucls = Counter(nucl for nucl in gene if nucl != "?")

if length % 4 != 0 or any(value > length / 4 for value in nucls.values()):
    print("===")
else:
    for letter in gene:
        if letter == "?":
            for nucl in nucls:
                if nucls[nucl] < length / 4:
                    print(nucl, end='')
                    nucls[nucl] += 1
                    break
        else:
            print(letter, end='')

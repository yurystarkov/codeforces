from re import sub

remix = input()

wubs = r"(WUB)+"

print(sub(wubs, " ", remix).strip())
